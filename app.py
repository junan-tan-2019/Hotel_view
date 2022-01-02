from flask import Flask, render_template, request, jsonify
from datetime import date, timedelta
import requests
import json
import ast


app = Flask(__name__)

image_list = [
    "https://pix8.agoda.net/hotelImages/124/1246280/1246280_16061017110043391702.jpg?s=1024x768"]


mock_room = {
    "roomNormalizedDescription": "Heritage Room",
    "free_cancellation": True,
    "roomAdditionalInfo": {"breakfastInfo": "hotel_detail_breakfast_included",
                           "displayFields": {"kaligo_service_fee": 0,
                                             "surcharges": [{"type": "TaxAndServiceFee", "amount": 756.00}]
                                             }
                           },
    "price": 123.55,
    "chargeableRate": 98.00,
    "points": 53000,
    "images": {0 :{"url": image_list[0]}},
    "amenities": ["Room size (sqm)", "Living room", "Internet access"]
}


@app.route("/home/<country_id>", methods=["GET"])
def hello_world(country_id):
    # id=WD0M
    url = "https://hotelapi.loyalty.dev/api/hotels?destination_id=" + country_id
    hotels_response = requests.get(url)
    jresponse = hotels_response.text
    data = json.loads(jresponse)

    image = image_list[0]

    return render_template("index.html", hotels=json.dumps(data), image=image)

#0dAF #another hotelid
# https://hotelapi.loyalty.dev/api/hotels/diH7
@app.route("/home/hotel/<hotel_id>", methods=["GET"])
def getHotel(hotel_id):
    url = "https://hotelapi.loyalty.dev/api/hotels/" + hotel_id
    hotel_response = requests.get(url)
    jresponse = hotel_response.text
    data = json.loads(jresponse)

    checkin_date = str(date.today())
    checkout_date = str(date.today() + timedelta(days=1))
    url_checkin_date = "checkin=" + checkin_date
    url_checkout_date = "checkout=" + checkout_date

    params = "/price?destination_id=WD0M&" + url_checkin_date + \
        "&" + url_checkout_date + \
        "&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1"

    room_list_url = "https://hotelapi.loyalty.dev/api/hotels/" + hotel_id + params
    room_list_response = requests.get(room_list_url)
    room_jresponse = room_list_response.text
    rooms_data = json.loads(room_jresponse)
    print(rooms_data)
    if len(rooms_data['rooms']) == 0:
        rooms_data['rooms'].append(mock_room)

    return render_template("hotel.html", hotel=data, room_list=rooms_data, checkin_date=checkin_date,
                           checkout_date=checkout_date)


@app.route("/home/room", methods=["GET"])
def viewRoom():
    hotel_name = request.args.get("hotel_name")
    data = request.args.get("room")
    room_data = ast.literal_eval(data)
    checkin_date = request.args.get("check_in_date")
    checkout_date = request.args.get("check_out_date")
    
    return render_template("room.html", room=room_data, hotel_name=hotel_name, 
                           checkin_date=checkin_date, checkout_date=checkout_date)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
