from flask import Flask, render_template, Blueprint, request, redirect

from models.publisher import Publisher
import repositories.publisher_repository as publisher_repository

publishers_blueprint = Blueprint("publishers", __name__)

@publishers_blueprint.route("/publishers") #index
def publishers():
  publishers = publisher_repository.select_all()
  return render_template("publishers/index.html", publishers = publishers)

@publishers_blueprint.route("/publishers/<id>") #show
def show(id):
  publisher = publisher_repository.select(id)
  return render_template("publishers/show.html", publisher = publisher)

@publishers_blueprint.route("/publishers/new", methods=["GET"]) #new
def new_publisher():
  return render_template("publishers/new.html")

@publishers_blueprint.route("/publishers", methods = ["POST"]) #create
def create_publisher():
  name = request.form["name"]
  address = request.form["address"]
  phone_number = request.form["phone_number"]
  new_publisher = Publisher(name, address, phone_number)
  publisher_repository.save(new_publisher)
  return redirect("/publishers")

@publishers_blueprint.route("/publishers/<id>/edit") #edit
def edit_publisher(id):
  publisher = publisher_repository.select(id)
  return render_template('publishers/edit.html', publisher = publisher)



@publishers_blueprint.route("/publishers/<id>", methods = ["POST"]) #update
def update_publisher(id):
  name = request.form["name"]
  address = request.form["address"]
  phone_number = request.form["phone_number"]
  publisher = Publisher(name, address, phone_number)
  publisher_repository.update(publisher)
  return redirect("/publishers")

@publishers_blueprint.route("/publishers/<id>/delete", methods = ["POST"]) #delete
def delete_publisher(id):
  publisher_repository.delete(id)
  return redirect("/publishers")