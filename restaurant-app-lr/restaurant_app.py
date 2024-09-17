from flask import Flask, render_template, request, url_for, abort, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sushi_model import Base_sushi, Sushi
from main_plate_model import Base_main_plate, Plate
from order_model import Base_order, Order

app = Flask(__name__)

engine_sushi = create_engine("sqlite:///sushis.db")
Base_sushi.metadata.create_all(engine_sushi)
Session_sushi = sessionmaker(bind=engine_sushi)
session_sushi = Session_sushi()

engine_main_plate = create_engine("sqlite:///main_plates.db")
Base_main_plate.metadata.create_all(engine_main_plate)
Session_main_plate = sessionmaker(bind=engine_main_plate)
session_main_plate = Session_main_plate()

engine_order = create_engine("sqlite:///orders.db")
Base_order.metadata.create_all(engine_order)
Session_order = sessionmaker(bind=engine_order)
session_order = Session_order()

@app.route("/")
def welcome_page():
    return render_template("welcome_page.html", main_menu_url=url_for("main_menu_page"))

@app.route("/regenerate_database/")
def regenerate_database():
    session_sushi.query(Sushi).delete()
    session_main_plate.query(Plate).delete()
    session_sushi.commit()
    session_main_plate.commit()

    sushis = [
        Sushi(type="Salmon", image="../static/images/sushis/salmon.png", price=11.6),
        Sushi(type="Crab", image="../static/images/sushis/crab.png", price=10.5),
        Sushi(type="Tuna", image="../static/images/sushis/tuna.png", price=12.9),
        Sushi(type="Seaweed", image="../static/images/sushis/seaweed.png", price=9.3),
        Sushi(type="California", image="../static/images/sushis/california.png", price=12.6)
    ]
    for sushi in sushis:
        session_sushi.add(sushi)
    session_sushi.commit()

    main_plates = [
        Plate(type="Fried egg plant", image="../static/images/main_menu/fried_egg_plant.png", url="#"),
        Plate(type="Meat with rice", image="../static/images/main_menu/meat_with_rice.png", url="#"),
        Plate(type="Oyacondon", image="../static/images/main_menu/oyacondon.png", url="#"),
        Plate(type="Rice with beef", image="../static/images/main_menu/rice_with_beef.png", url="#"),
        Plate(type="Sushi", image="../static/images/main_menu/sushi.png", url="sushis.html")
    ]
    for plate in main_plates:
        session_main_plate.add(plate)
    session_main_plate.commit()

    return "Database regenerated successfully!"

@app.route("/main_menu_page/")
def main_menu_page():
    main_plates = session_main_plate.query(Plate).all()
    main_plates_json = [plate.toJSON() for plate in main_plates]
    return render_template("main_menu.html", main_plates=main_plates_json)

@app.route("/sushis/")
def sushi_page():
    sushis = session_sushi.query(Sushi).all()
    sushis_json = [sushi.toJSON() for sushi in sushis]
    return render_template("sushi_menu.html", sushis=sushis_json)

@app.route("/order_request/", methods=["POST"])
def order_request():
    order_summary = request.form["order_summary"]
    order_items = order_summary.split("\n")
    customer_name = request.form["customer_name"]

    new_order = Order(customer_name=customer_name, orders=order_summary)
    try:
        session_order.add(new_order)
        session_order.commit()
        return render_template("order_summary.html", order_items=order_items, customer_name=customer_name)
    except:
        return "There was an issue adding your order"

@app.route("/kitchen/")
def kitchen():
    orders = session_order.query(Order).order_by(Order.date_created).all()
    orders_json = [order.toJSON() for order in orders]
    return render_template("kitchen.html", orders=orders_json)

@app.route("/delete/<int:id>")
def delete(id):
    order_to_delete = session_order.query(Order).get(id)
    if order_to_delete is None:
        abort(404)
    try:
        session_order.delete(order_to_delete)
        session_order.commit()
        return redirect(url_for("kitchen"))
    except:
        return "There was a problem deleting that order"
if __name__ == "__main__":
    app.run(debug=True)