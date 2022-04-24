def serialize_guides(guides):
    
    guides_list = []

    for guide in guides:
        guides_list.append({
        'id' : guide.id,
        'date' : guide.date.strftime('%Y-%m-%d %H:%M:%S'),

        })

    return guides_list

