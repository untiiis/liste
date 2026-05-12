import requests
from bs4 import BeautifulSoup
import re

def recuperer_lien_iptv(url_page):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url_page, headers=headers)
    
    if response.status_code != 200:
        print(f"Erreur HTTP : {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    all_text = soup.get_text()
    
    liens = re.findall(r'http[s]?://\S*m3u_plus\S*', all_text)
    
    if liens:
        return liens[0]
    else:
        print("Aucun lien IPTV trouvé sur la page.")
        return None

def mettre_a_jour_fichier_pp(nom_fichier, nouveau_lien):
    try:
        with open(nom_fichier, 'r') as f:
            lignes = f.readlines()

        if len(lignes) < 2:
            lignes.append(nouveau_lien + '\n')
        else:
            lignes[1] = nouveau_lien + '\n'

        with open(nom_fichier, 'w') as f:
            f.writelines(lignes)

        print(f"Fichier {nom_fichier} mis à jour avec le nouveau lien.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour du fichier : {e}")

if __name__ == "__main__":
    url = "https://ptiptv.com/topic/39-%F0%9F%9A%80-ptiptv-free-iptv-account-%E2%80%93-for-members-only-daily-update/"
    lien_iptv = recuperer_lien_iptv(url)
    if lien_iptv:
        mettre_a_jour_fichier_pp("pp.txt", lien_iptv)
