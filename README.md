# InnVentory
Hotel Inventory management

## Installation
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. create secret.ini as sample.ini with credentials
4. Run the server

```bash
git clone
cd InnVentory
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Features
- [x] MySQL Database
- [x] Add new Inventory
- [x] Update Inventory
- [x] Authorization and Authentication View
- [x] Inventory List View
- [x] Inventory Pagination
- [x] Search Inventory by hotel_name
- [x] Filter Inventory by hotel_id, room_id, available
- [x] Import bulk Inventories
- [x] Export Inventories
