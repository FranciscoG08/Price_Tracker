import re

def limpeza_preco(preco):
    preco_num = re.sub(r'[^\d.,]', '',preco)
    return preco_num.strip()

def worten(page):
    try:
        # --- Nome ---
        page.wait_for_selector('[class="product-header__title"]', state="attached", timeout=15000)
        nome = page.locator('[class="product-header__title"]').first.inner_text()

        # --- Preco Unidades ---
        page.wait_for_selector('[class="value"]', state="attached", timeout=15000)
        preco1 = page.locator('[class="value"]').first.inner_text()
        # --- Preco Decimais ---
        page.wait_for_selector('[class="decimal"]', state="attached", timeout=15000)
        preco2 = page.locator('[class="decimal"]').first.inner_text()

        # --- Limpeza Preço Worten ---
        preco_final = preco1.strip() + "," + preco2.strip()

        return {"name": nome, "store": "Worten", "price": preco_final}
    except: return None

def puma(page):
    try:
        # --- Nome ---
        page.wait_for_selector('[class="product-name"]', state="attached", timeout=15000)
        nome = page.locator('[class="product-name"]').first.inner_text()

        # -- Preco ---
        page.wait_for_selector('[class="value"]', state="attached", timeout=15000)
        preco1 = page.locator('[class="value"]').first.inner_text()

        # --- Limpeza Preço ---
        preco_final = limpeza_preco(preco1)
        
        return {"name": nome, "store": "Puma", "price": preco_final}
    except: return None
     
def adidas(page):
    try:
        # --- Nome ---
        page.wait_for_selector('[data-testid="product-title"]', state="attached", timeout=15000)
        nome = page.locator('[data-testid="product-title"]').first.inner_text()

        # -- Preco ---
        page.wait_for_selector('[data-testid="main-price"]', state="attached", timeout=15000)
        preco1 = page.locator('[data-testid="main-price"]').first.inner_text()

        # --- Limpeza Preço ---
        preco_final = limpeza_preco(preco1) 

        return {"name": nome, "store": "Adidas", "price": preco_final}
    except: return None

def nike(page):
    try:
        # --- Nome ---
        page.wait_for_selector('[data-testid="product_title"]', state="attached", timeout=15000)
        nome = page.locator('[data-testid="product_title"]').first.inner_text()

        # -- Preco ---
        page.wait_for_selector('[data-testid="currentPrice-container"]', state="attached", timeout=15000)
        preco1 = page.locator('[data-testid="currentPrice-container"]').first.inner_text()

        # --- Limpeza Preço ---
        preco_final = limpeza_preco(preco1) 

        return {"name": nome, "store": "Nike", "price": preco_final}
    except: return None

def ikea(page):
    try:
        # --- Nome ---
        page.wait_for_selector('.pipcom-price-module__information h1', state="attached", timeout=15000)
        nome = page.locator('.pipcom-price-module__information h1').first.inner_text()

        # -- Preco ---
        page.wait_for_selector('.pipcom-price__sr-text', state="attached", timeout=15000) #Seletor da class CSS (.*classe*)
        preco1 = page.locator('.pipcom-price__sr-text').first.inner_text()

        # --- Limpeza Preço ---
        preco_final = limpeza_preco(preco1) 

        return {"name": nome, "store": "Ikea", "price": preco_final}
    except:
        return None

def pcdiga(page):
    try:
        # --- Nome ---
        page.wait_for_selector('h1', state='attached', timeout=15000)
        nome = page.locator('h1').first.inner_text()

        # --- Preço ---
        page.wait_for_selector('div[class*="text-primary"][class*="font-black"]', timeout=15000)
        preco1 = page.locator('div[class*="text-primary"][class*="font-black"]').first.inner_text()


        # --- Limpeza do preço ---
        preco_final = limpeza_preco(preco1)

        return {"name": nome, "store": "PcDiga", "price": preco_final}
    except Exception as e:
        print("Erro:", e)

def amazon(page):
    try:
        # --- Nome ---
        page.wait_for_selector('[id="productTitle"]', timeout=15000)
        nome = page.locator('[id="productTitle"]').first.inner_text()
        # --- Preço ---
        page.wait_for_selector('#corePrice_feature_div .a-offscreen', timeout=15000)
        preco1 = page.locator('#corePrice_feature_div .a-offscreen').first.inner_text()

        # --- Limpeza do preço ---
        preco_final = limpeza_preco(preco1)

        return {"name": nome, "store": "AmazonEs", "price": preco_final}
    except:
        return None

def samsung(page):
    try:
        # --- Nome ---
        url = page.url
        nome = url.split("/")[5]
        nome = nome.replace("-"," ").title()

        # --- Preço (qualquer elemento que tenha €) ---
        selector_data = "[data-discountprice], [data-modelprice], [data-modelrevenue]"
        # Espera até 5 segundos por um desses atributos
        page.wait_for_selector(selector_data, state="attached", timeout=5000)
        elemento_preco = page.locator(selector_data).first
            
        # Prioridade: Preço com desconto > Preço do modelo
        preco1 = (elemento_preco.get_attribute("data-discountprice") or 
                    elemento_preco.get_attribute("data-modelprice") or
                    elemento_preco.get_attribute("data-modelrevenue"))
        
        # --- Limpeza do preço ---
        preco1 = preco1.replace('.',',')
        preco_final = limpeza_preco(preco1)

        return {"name": nome, "store": "Samsung", "price": preco_final}
    except Exception as e:
        print("Erro:", e)

def sportZone(page):
    try:
        # --- Nome ---
        page.wait_for_selector('[data-element="product-name"]', timeout=15000)
        nome = page.locator('[data-element="product-name"]').first.inner_text()
        # --- Preço ---
        page.wait_for_selector('[data-element="product-price"]', timeout=15000)
        preco1 = page.locator('[data-element="product-price"]').first.inner_text()

        # --- Limpeza do preço ---
        preco_final = limpeza_preco(preco1)

        return {"name": nome, "store": "SportZone", "price": preco_final}
    except Exception as e:
        print("Erro:", e)

def radioPopular(page):
    try:
        # --- Nome ---
        page.wait_for_selector('#designation p', state='attached', timeout=15000)
        nome = page.locator('#designation p').first.inner_text()
        # Remove texto extra do small
        nome = nome.split('(')[0].strip()

        # --- Preço ---
        page.wait_for_selector('#product-value', state='attached', timeout=15000)
        preco1 = page.locator('#product-value').first.get_attribute('value')

        # --- Limpeza do preço ---
        preco1 = preco1.replace('.',',')
        preco_final = limpeza_preco(preco1)

        return {"name": nome, "store": "RadioPopular", "price": preco_final}
    except Exception as e:
        print("Erro:", e)