from flask import Flask, redirect, render_template_string
from datetime import datetime, timedelta

app = Flask(__name__)

URL_CIBLE = "https://iptv-org.github.io/iptv/index.country.m3u"  
DATE_DEBUT = "2026-05-27"

@app.route("/")
def index():
    debut = datetime.strptime(DATE_DEBUT, "%Y-%m-%d")
    maintenant = datetime.now()
    
    if maintenant <= debut + timedelta(days=7):
        return redirect(URL_CIBLE)
    else:
        return render_template_string("""
            <h2 style="text-align:center; margin-top:50px; font-family:sans-serif;">
                Accès expiré ❌<br><br>
                L’abonnement de 7 jours est terminé.
            </h2>
        """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
