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

def recuperer_playlist_complete(url_playlist):
    try:
        response = requests.get(url_playlist)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Erreur lors de la récupération de la playlist complète : {e}")
        return None

def ecrire_playlist_dans_fichier(nom_fichier, contenu_playlist):
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            f.write(contenu_playlist)
        print(f"Fichier {nom_fichier} mis à jour avec la playlist complète.")
    except Exception as e:
        print(f"Erreur lors de l’écriture dans le fichier : {e}")

if __name__ == "__main__":
    url_page = "https://ptiptv.com/topic/112-🚀-ptiptv-free-educational-iptv-test-playlist-xtream-codes-100-user-🟢/"
    lien_iptv = recuperer_lien_iptv(url_page)
    if lien_iptv:
        print(f"Lien IPTV trouvé : {lien_iptv}")
        contenu_playlist = recuperer_playlist_complete(lien_iptv)
        if contenu_playlist:
            print(f"Contenu playlist récupéré, taille : {len(contenu_playlist)} caractères")
            ecrire_playlist_dans_fichier("pp.txt", contenu_playlist)
