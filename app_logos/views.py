from django.shortcuts import render_to_response


TABS = {
    'nutrition' : ['bio', 'demeter', 'naturland'],
    'textiles' : ['link1', 'link2', 'link3'],
    'cosmetics' : [],
    'paper' : ['blauer_engel', 'oekopaplus', 'fsc_recycling'],
    'misc' : [],
}

def logo_details(request, menu, tab=None):
    data = { 'menu' : ['nutrition', 'textiles', 'cosmetics', 'paper', 'misc'],
             'tabs' : TABS[menu],
             'selected_menu' : menu,
             'selected_tab' : tab }

    if menu in data['menu']:
        if tab in TABS[menu]:
            return render_to_response('logo_pages/%s.html' % menu, data)
        else:
            data['selected_tab'] = TABS[menu][0]
            return render_to_response('logo_pages/%s.html' % menu, data)
    else:
        raise Http404
