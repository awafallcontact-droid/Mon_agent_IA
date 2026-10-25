import smtplib
from email.message import EmailMessage
import os
import requests
from dotenv import load_dotenv
from tavily import TavilyClient
from notion_client import Client 

# Charge les variables cachées dans le fichier .env
load_dotenv()

# Récupère la clé API Tavily
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Initialise l'outil Tavily
tavily_client = TavilyClient(api_key=tavily_api_key)

def search_web(query: str):
    """Recherche des informations sur Internet via Tavily."""
    print(f"Recherche en cours pour : '{query}'...")
    
    # Exécute la recherche
    response = tavily_client.search(query=query)
    
    return response

# ... (votre code précédent)

# --- Configuration WeatherAPI ---
weather_api_key = os.getenv("WEATHER_API_KEY")

def get_weather(city: str):
    """Récupère la météo actuelle pour une ville donnée via WeatherAPI."""
    print(f"Consultation de la météo pour : {city}...")
    
    # L'URL de l'API avec la ville, la clé et la langue française
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}&lang=fr"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # On extrait seulement les informations utiles pour l'agent
        return {
            "ville": data["location"]["name"],
            "pays": data["location"]["country"],
            "temperature_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"]
        }
    else:
        return f"Erreur : Impossible de récupérer la météo (Code {response.status_code})"


# --- Configuration Notion ---

notion_api_key = os.getenv("NOTION_API_KEY")
notion = Client(auth=notion_api_key)

def search_notion(query: str):
    """Recherche des pages dans le Notion de l'utilisateur."""
    print(f"Recherche dans Notion pour : '{query}'...")
    try:
        response = notion.search(query=query).get("results")
        pages = [{"id": p.get("id"), "url": p.get("url")} for p in response]
        return pages if pages else "Aucune page trouvée. Avez-vous partagé la page avec l'intégration ?"
    except Exception as e:
        return f"Erreur : {str(e)}"

# --- Configuration Email ---
email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")

def send_email(destinataire: str, sujet: str, contenu: str):
    """Envoie un email via Gmail."""
    print(f"Envoi d'un email à {destinataire}...")
    
    msg = EmailMessage()
    msg.set_content(contenu)
    msg['Subject'] = sujet
    msg['From'] = email_sender
    msg['To'] = destinataire

    try:
        # Connexion au serveur SMTP de Gmail
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email_sender, email_password)
        server.send_message(msg)
        server.quit()
        return f"Email envoyé avec succès à {destinataire} !"
    except Exception as e:
        return f"Erreur lors de l'envoi de l'email : {str(e)}"



    
# Petit test pour voir si ça marche
if __name__ == "__main__":
    resultat = search_web("Quelles sont les dernières actualités sur l'IA au Sénégal ?")
    print(resultat)

    # Test de la météo
    resultat_meteo = get_weather("Dakar")
    print("\n--- Résultat Météo ---")
    print(resultat_meteo)         

    # Test de la recherche Notion
    print(search_notion(""))


# Remplacez par une adresse email valide pour tester
    resultat = send_email("test@example.com", "Test Agent IA", "Ceci est un test depuis Python.")
    print(resultat)