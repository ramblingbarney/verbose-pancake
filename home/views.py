from django.shortcuts import render
from django.db.models import Count
from django.contrib.auth.models import User
from products.models import Product
import math
import json


def index(request):
    '''
    A view that displays the index page
    '''

    background_colour_list = [
                    'rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)']

    border_colour_list = [
        'rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)']

    # all votes

    all_votes = Product.objects.values('name').annotate(Count('productvote__user_id')).filter(productvote__user_id__count__gt=0)

    all_product_names_all_votes = []
    all_product_all_votes = []

    for i, q in enumerate(all_votes):
        all_product_names_all_votes.append(str(q['name']))
        all_product_all_votes.append(str(q['productvote__user_id__count']))

    if len(all_product_names_all_votes) == 0:
        all_product_names_all_votes = ['No Data']
        all_product_all_votes = ['0']

    bg_colours = background_colour_list * math.ceil((len(all_product_names_all_votes) / len(background_colour_list)))
    b_colours = border_colour_list * math.ceil((len(all_product_names_all_votes) / len(border_colour_list)))

    json_all_product_names_all_votes = json.dumps(all_product_names_all_votes)
    json_all_product_all_votes = json.dumps(all_product_all_votes)
    json_bg_colours_all_votes = json.dumps(bg_colours[:len(all_product_names_all_votes)])
    json_b_colours_all_votes = json.dumps(b_colours[:len(all_product_names_all_votes)])

    # donations

    all_donations = Product.objects.values('name','total_amount_paid').filter(total_amount_paid__gt=1)

    all_product_names_donations = []
    all_product_donations = []

    for i, q in enumerate(all_donations):
        all_product_names_donations.append(str(q['name']))
        all_product_donations.append(str(q['total_amount_paid']))

    if len(all_product_names_donations) == 0:
        all_product_names_donations = ['No Data']
        all_product_donations = ['0']

    bg_colours = background_colour_list * math.ceil((len(all_product_names_donations) / len(background_colour_list)))
    b_colours = border_colour_list * math.ceil((len(all_product_names_donations) / len(border_colour_list)))

    json_all_product_names_donations = json.dumps(all_product_names_donations)
    json_all_product_donations = json.dumps(all_product_donations)
    json_bg_colours_donations = json.dumps(bg_colours[:len(all_product_names_donations)])
    json_b_colours_donations = json.dumps(b_colours[:len(all_product_names_donations)])

    args = {
            'all_product_names_all_votes': json_all_product_names_all_votes,
            'all_product_all_votes': json_all_product_all_votes,
            'background_colours_all_votes': json_bg_colours_all_votes,
            'border_colours_all_votes': json_b_colours_all_votes,

            'all_product_names_donations': json_all_product_names_donations,
            'all_product_donations': json_all_product_donations,
            'background_colours_donations': json_bg_colours_donations,
            'border_colours_donations': json_b_colours_donations,
            }
    return render(request, 'index.html', args)
