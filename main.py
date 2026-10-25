import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # NOUVEAU : Importation du CORS
from pydantic import BaseModel
from pydantic_ai import Agent
from dotenv import load_dotenv

# Importation de vos 4 outils depuis tools.py
from tools import search_web, get_weather, search_notion, send_email

load_dotenv()

# 1. Configuration du modèle pour utiliser la passerelle et la clé RodiumAi
os.environ["OPENAI_BASE_URL"] = "https://api.rodiumai.io/v1"


# 2. Création de l'application web
app = FastAPI(title="Mon Agent IA Rodium")

# NOUVEAU : Configuration du CORS pour autoriser l'interface web (GitHub) à communiquer avec l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet à n'importe quel site (y compris GitHub Pages) de s'y connecter
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# 3. Création du cerveau de l'agent avec le modèle RodiumAi
agent = Agent(
    'openai:openai/gpt-4o-mini',
    system_prompt="Tu es un assistant IA personnel très compétent. Tu as accès à internet, à la météo, au Notion de l'utilisateur et tu peux envoyer des emails. Utilise ces outils intelligemment pour répondre aux requêtes."
)

# 4. Ajout des outils à l'agent (utilisation de tool_plain pour les fonctions sans contexte)
agent.tool_plain(search_web)
agent.tool_plain(get_weather)
agent.tool_plain(search_notion)
agent.tool_plain(send_email)

# 5. Format de la requête HTTP
class ChatRequest(BaseModel):
    message: str

# 6. Route principale pour discuter
@app.post("/chat")
async def discuter_avec_agent(requete: ChatRequest):
    print(f"\n--- Nouveau message reçu : {requete.message} ---")
    
    # L'agent analyse la question et choisit ses outils
    resultat = await agent.run(requete.message)
    
    return {"reponse":resultat.output} 

# 7. Route de vérification (Accueil)
@app.get("/")
def accueil():
    return {"statut": "Le serveur de l'Agent IA est en ligne !"}
