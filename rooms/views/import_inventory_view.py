from django.views.generic import View
import csv
from io import StringIO
from django.shortcuts import render, redirect
from django.contrib import messages


from rooms.managers.room_inventory_manager import RoomInventoryManager
from rooms.forms.csv_import_form import CsvImportForm

class ImportInventoryView(View):

    def __init__(self):
        self.room_inv_mng = RoomInventoryManager()

    def get(self, request):
        form = CsvImportForm()
        payload = {"form": form}

        return render(
            request, "import_inventory.html", payload
        )

    def post(self, request):

        csv_file = request.FILES["csv_file"]

        csv_format = ['Hotel ID', 'Hotel Name', 'Room ID', 'Date', 'Available']

        csv_file.seek(0)
        reader = csv.reader(StringIO(csv_file.read().decode('utf-8')))
        header = next(reader)
        if header != csv_format:
            messages.error(request, "Mismatch in header")
        else:
            result = None
            for row in reader:
                result = self.room_inv_mng.create_inventory(row[0], row[1], row[2], row[3], row[4])
            messages.success(request, "Your csv file has been imported with " + str(result))

        return redirect("..")
