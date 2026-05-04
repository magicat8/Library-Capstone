# Library Database Management System

A comprehensive Django-based library database management system designed for senior capstone project. This system enables efficient management of book inventory, sales tracking, customer requests, and detailed reporting for library operations.

## Features

### Core Inventory Management
- **Book Catalog**: Maintain detailed information about each book including title, author, ISBN, publisher, description, and condition
- **ISBN Lookup**: Automatic book data retrieval from Google Books API using ISBN numbers
- **Inventory Tracking**: Real-time inventory management with copy counts and condition categorization (New, Like New, Good, Acceptable)
- **Pricing**: Track and manage book prices

### Sales & Reporting
- **Sales Tracking**: Record and monitor book sales with automatic inventory updates
- **Sales Reports**: Generate detailed sales reports with date range filtering including:
  - Books sold during the period
  - Inventory turnover rates
  - Total sales volume
  - Average turnover metrics
- **Unsold Books Report**: Identify books that haven't sold within a specified time period (configurable by months)
- **Book List View**: Browse complete inventory with filtering by condition and availability

### Customer Management
- **Customer Requests**: Track customer book requests with customer contact information
- **Request Tracking**: Store ISBN and book title requests with customer email and date

### Additional Features
- **Barcode Scanning**: Support for scanning barcodes to add/update inventory
- **Admin Interface**: Django admin panel with customized book management interface
- **Database Persistence**: SQLite database for reliable data storage

## Technology Stack

- **Framework**: Django 5.2.6
- **Database**: SQLite3
- **Language**: Python 3.x
- **Frontend**: HTML/CSS with Jinja2 templates
- **APIs**: Google Books API for ISBN lookups
- **Libraries**:
  - `isbnlib`: ISBN validation and utilities
  - `requests`: HTTP requests for API calls
  - `beautifulsoup4`: Web scraping capabilities

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Library-Capstone
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the Django project**
   ```bash
   cd library_database
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```
   if using production server use
   ```bash
   gunicorn --bind 0.0.0.0:8000 --workers 3 library_database.wsgi:application &
   ```

9. **Access the application**
   - Website: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

## Project Structure

```
Library-Capstone/
├── library_database/           # Django project root
│   ├── manage.py              # Django management script
│   ├── db.sqlite3             # Database file
│   ├── books/                 # Books app
│   │   ├── models.py          # Data models (Book, Sale, ISBNEntry, CustomerRequest)
│   │   ├── views.py           # View functions and logic
│   │   ├── admin.py           # Django admin configuration
│   │   ├── migrations/        # Database migrations
│   │   ├── templates/         # HTML templates
│   │   │   └── books/
│   │   │       ├── index.html
│   │   │       ├── book_list.html
│   │   │       ├── sales_report.html
│   │   │       └── unsold_books_report.html
│   │   └── static/            # CSS and JavaScript
│   ├── other/                 # Other products app (movies, etc.)
│   ├── library_database/      # Project configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── staticfiles/           # Compiled static files
├── requirements.txt           # Python dependencies
├── isbn_lookup_test.py        # ISBN lookup testing script
├── scan_test.py               # Barcode scanning testing script
├── scanned_barcodes.csv       # Scanned barcodes log
└── README.md                  # This file
```

## Models

### Book
Represents a book in the library inventory with fields:
- `title`, `author`, `isbn`, `publisher`
- `published_year`, `page_count`, `language`
- `description`, `categories`
- `condition` (choices: New, Like New, Good, Acceptable)
- `copies` (quantity in stock)
- `price`

### Sale
Tracks book sales with:
- Reference to the book sold
- Quantity sold
- Sale date (auto-recorded)
- Auto-updates inventory on creation/deletion

### ISBNEntry
Manages ISBN-to-book conversion:
- Accepts ISBN and condition
- Automatically fetches book data from Google Books API
- Creates or updates Book records
- Increments copy count if book already exists

### CustomerRequest
Stores customer book requests:
- Customer name and email
- Requested book title and/or ISBN
- Request date

## Usage Examples

### Add a Book via ISBN
1. Go to Admin Panel → Books → ISBN Entries
2. Enter ISBN and select condition
3. System automatically retrieves book details and adds to inventory

### Generate Sales Report
1. Navigate to Sales Report page
2. Select start and end dates
3. View sales volume, inventory, and turnover rates

### Find Unsold Books
1. Navigate to Unsold Books Report
2. Choose time period (default 6 months)
3. Review books with no sales activity

## Future Enhancement Ideas

- **Customer Hold System**: Allow customers to place holds on books through the website
- **Multi-location Support**: Use Tailscale network to link database across multiple library locations
- **Scalability**: Implement network solutions for distributed database access
- **Weight/Scale Tracking**: Integrate scale data for inventory verification
- **Customer Portal**: Enhanced customer interface for requests and holds

## Testing

Test scripts are included for specific functionalities:
- `isbn_lookup_test.py`: Test ISBN lookup integration
- `scan_test.py`: Test barcode scanning functionality

Run tests with:
```bash
python isbn_lookup_test.py
python scan_test.py
```

## Admin Features

The Django admin interface provides:
- Full CRUD operations on all models
- Customized book admin interface
- Sales and request management
- Data filtering and searching
- Bulk actions for inventory updates

## Contributing

This is a capstone project. Contact the development team for contribution guidelines.

## License

See LICENSE file for details.

## Support

For issues or questions, please open an issue in the repository or contact the development team. 
