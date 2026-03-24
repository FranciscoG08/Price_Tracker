from google_apis import get_sheet_data, add_new_product_row,update_product_price
from play_wright import get_product_data,cleaned_link
from email_sender import send_email
import time

def main():
    start_time = time.time()  # Marca o tempo inicial
    print("=======START=======")

    sheet_name = "Price_Tracker"
    print("A Ler ficheiro ", sheet_name)

    data, sheet = get_sheet_data(sheet_name) #data retorna tudo em forma dicionario, sheet é o Objeto
    alerts = []

    #Loop pelos dados do GoogleSheets(cada linha é um dicionario)
    #{'Link': 'https://www.amazon.es/-/pt/dp/B0DSLBN5FS/?_encoding=UTF8&ref_=pd_hp_d_atf_unk', 'Category': '', 'Name': '', 'First_price': '', 'Lastest_price': ''}
    for index, row in enumerate(data,start=2): #start=2 porque a row 1 são cabeçalhos
        link = row.get('Link') # Pega o link do dicionario 'Link': 'https://www.amazon.es/-/pt/dp/B0DSLBN5FS/?_encoding=UTF8&ref_=pd_hp_d_atf_unk', 'Category': '', ...}

        if not link:
            continue
        print("A verificar: ",link)
        
        #LIMPAR URL antes de mandar
        clean_link = cleaned_link(link)
        
        product = get_product_data(link, clean_link)
        
        if not product:
            print("Erro ao Obter produto")
            continue

        name = product['name']
        store = product['store']
        price = round(
            float(str(product['price']).replace('.', '').replace(',', '.')),
            2
        )
                
        #GOOGLE SHEET EM INGLES USAR:
        #first_price = float(row.get('First_price'))
        #last_price = float(row.get('Lastest_price'))
        
        #GOOGLE SHEET EM PORTUGUES USAR:
        first_price = float(str(row.get('First_price') or 0).replace(',', '.'))
        last_price = float(str(row.get('Lastest_price') or 0).replace(',', '.'))
        
        #Produto novo ainda nao adicionado
        if not first_price:
            first_price = price
            last_price = price
            add_new_product_row(sheet,index,store,name,first_price,last_price)
            print("Produto Novo adicionado")

        if(price < first_price):
            preco_anterior=price
            print(f"Alerta\n\t->Produto: {name}\n\t-> Novo Preco {price:.2f}")
            #Adicionar à lista alertas -> Será o formato que aparecerá no Mail
            alerts.append(
                f"O produto: {name}\nBaixou de {preco_anterior:.2f}€ para {price:.2f}€\nLink:{link}"
            )
            # Atualizamos as variáveis para gravar na folha
            last_price = price

            update_product_price(sheet,index,first_price,last_price)
        else:
            print(f"Sem alteração (Atual: {price:.2f}€ | Anterior: {first_price:.2f}€)")
            # Opcional: atualizar o last_price mesmo que o preço suba ou seja igual
            update_product_price(sheet, index, first_price, price)
    
    if alerts:
            send_email("\n".join(alerts))
        
    print("=======END=======")
    end_time = time.time()  # Marca o tempo final
    elapsed_time = end_time - start_time
    print(f"Tempo total de execução: {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    main()