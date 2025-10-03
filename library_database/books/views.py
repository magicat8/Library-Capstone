from django.shortcuts import render

def index(request):
    return render(request, 'books/index.html')

from .models import Book, Sale
from django.db.models import Sum
from datetime import datetime, timedelta

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def sales_report(request):
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    
    report_data = []
    total_sales = 0
    total_turnover = 0

    if start_date_str and end_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        sales = Sale.objects.filter(sale_date__range=[start_date, end_date])\
            .values('book__title', 'book__author', 'book__copies')\
            .annotate(sold_copies=Sum('quantity'))

        for sale in sales:
            # copies_on_hand is end of period inventory
            copies_on_hand = sale['book__copies']
            sold_copies = sale['sold_copies']
            
            # Estimate start of period inventory
            start_inventory = copies_on_hand + sold_copies
            
            # Avoid division by zero
            average_inventory = (start_inventory + copies_on_hand) / 2
            turnover_rate = sold_copies / average_inventory if average_inventory else 0

            report_data.append({
                'title': sale['book__title'],
                'author': sale['book__author'],
                'copies_on_hand': copies_on_hand,
                'sold_copies': sold_copies,
                'turnover_rate': turnover_rate,
            })

        if report_data:
            total_sales = sum(item['sold_copies'] for item in report_data)
            total_turnover = sum(item['turnover_rate'] for item in report_data) / len(report_data)

    context = {
        'report_data': report_data,
        'start_date': start_date_str,
        'end_date': end_date_str,
        'total_sales': total_sales,
        'total_turnover': total_turnover,
    }
    return render(request, 'books/sales_report.html', context)

def unsold_books_report(request):
    months_str = request.GET.get('months', '6')
    months = int(months_str)

    cutoff_date = datetime.now().date() - timedelta(days=30 * months)

    # Books that have sold in the last X months
    sold_book_ids = Sale.objects.filter(sale_date__gte=cutoff_date).values_list('book_id', flat=True).distinct()

    # Books that have NOT sold
    unsold_books = Book.objects.exclude(id__in=sold_book_ids).order_by('categories', 'title')

    context = {
        'unsold_books': unsold_books,
        'months': months,
    }
    return render(request, 'books/unsold_books_report.html', context)