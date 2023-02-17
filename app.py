from flask import Flask, url_for, render_template, request, session, redirect, flash, g, jsonify
import json
import math
import datetime
import os
from timber import TimberRectangleCS


template_dir = os.path.abspath("Templates")

app = Flask(__name__, template_folder=template_dir)
app.config["SECRET_KEY"] = "SomethingWhatNo1CanGuess!"
cache = {}

#Timber classes for the select field in construction_definition.html
timber_classes = ["C14", "C16", "C18", "C22", "C24", "C27", "C30", "C35", "C40", "C45", "C50", "D30", "D35", "D40", "D50", "D60", "D70"]




@app.route("/")
def index():
    
    if "sparre" in cache.keys():
        print(cache["sparre"].area)
        
    if "pfette" in cache.keys():
        print(cache["pfette"].area)

    if "bending_moment" in cache.keys():
        print(cache["bending_moment"])
    
    return render_template("index.html", active_menu="Home")

@app.route("/timber_construction", methods=["GET", "POST"])
def timber_construction(TimberCrossSectionClass = TimberRectangleCS):
    
    if request.method == "GET":
        return render_template("construction_definition.html", timber_classes = timber_classes, active_menu = "Dachstuhldefinition")

    else:
        ###################### Sparren ######################
        sparren_holz_klasse = "C14"
        if "sparren_holz_klasse" in request.form:
            sparren_holz_klasse = request.form["sparren_holz_klasse"]
        
        sparrenBreite = 300
        if "sparrenBreite" in request.form:
            sparrenBreite = int(request.form["sparrenBreite"])

        sparrenHoehe = 300
        if "sparrenHoehe" in request.form:
            sparrenHoehe = int(request.form["sparrenHoehe"])

        sparrenAbstand = 6000
        if "sparrenAbstand" in request.form:
            sparrenAbstand = int(request.form["sparrenAbstand"])

        ###################### Pfetten ######################
        pfetten_holz_klasse = "C14"
        if "pfetten_holz_klasse" in request.form:
            pfetten_holz_klasse = request.form["pfetten_holz_klasse"]

        pfettenBreite = 300
        if "pfettenBreite" in request.form:
            pfettenBreite = int(request.form["pfettenBreite"])

        pfettenHoehe = 300
        if "pfettenHoehe" in request.form:
            pfettenHoehe = int(request.form["pfettenHoehe"]) 

        pfettenAbstand = 6000
        if "pfettenAbstand" in request.form:
            pfettenAbstand = int(request.form["pfettenAbstand"])

        
        
        sparre =  TimberCrossSectionClass(strength_class = sparren_holz_klasse, width = sparrenBreite, height = sparrenHoehe)
        pfette = TimberCrossSectionClass(strength_class = pfetten_holz_klasse, width = pfettenBreite, height = pfettenHoehe)

        cache["sparre"] = sparre
        cache["pfette"] = pfette
       
        flash("Querschnittsdaten wurden gespeichert")
        return redirect(url_for('index'))
        #return render_template("design_data.html", sparrenCrossSection = sparrenCrossSection, pfettenCrossSection = pfettenCrossSection)


@app.route("/internal_forces", methods=["GET", "POST"])
def internal_forces():
    if request.method == "GET":
        return render_template("internal_forces_definition.html", active_menu="Schnittgroessendefinition")

    else:
        ###################### Bending Moment ######################
        bending_moment = 100
        if "bending_moment" in request.form:
            bending_moment = request.form["bending_moment"]

        cache["bending_moment"] = bending_moment

        flash("Schnittgroessen wurden gespeichert")
        return redirect(url_for('index'))

@app.route("/calculation", methods=["GET"])
def calculate():
    return "{} - {}. The Bending Moment is {}".format(cache["pfette"].area, cache["sparre"].area, cache["bending_moment"])

