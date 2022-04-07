'''
formatação dos urls a ser usados para extração de dados

'''


from datetime import datetime, timedelta

today = datetime.today().strftime('%Y-%m-%d')
tomorrow = datetime.now() + timedelta(days=1)
tomorrow = tomorrow.strftime('%Y-%m-%d')

check_in = today
check_out = tomorrow

# para lisboa
url_lisboa = "https://www.airbnb.pt/s/Lisboa-~" \
             "-Cidade--Lisboa--Portugal/homes?tab_id=home_tab&ref" \
             "inement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%" \
             "5D=april&flexible_trip_dates%5B%5D=may&flexible_tri" \
             "p_lengths%5B%5D=weekend_trip&date_picker_type=ca" \
             "lendar" \
             "&checkin=" + check_in + "" \
             "&checkout=" + check_out + "" \
             "&fl" \
             "exible_date_search_filter_type=0&query=Lisboa%20-%20" \
             "Cidade%2C%20Lisboa%2C%20Portugal&place_id=EiFMaXNib2EgLSBDa" \
             "WRhZGUsIExpc2JvYSwgUG9ydHVnYWwiLiosChQKEgnrpgqMHTMZDRH0jG_ohiuDCxIU" \
             "ChIJO_PkYRozGQ0R0DaQ5L3rAAQ&source=structured_search_input_header&s" \
             "earch_type=autocomplete_click"

# para o porto
url_porto = "https://www.airbnb.pt/s/Porto-Central--Porto--Portugal/" \
"homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&" \
"flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may" \
"&flexible_trip_lengths%5B%5D=weekend_trip&" \
"date_picker_type=calendar" \
"&checkin=" + check_in + \
"&checkout=" + check_out + \
"&flexible_date_search_filter_type=0" \
"&source=structured_search_input_header" \
"&search_type=user_map_move" \
"&query=Porto%20Central%2C%20Porto" \
"%2C%20Portugal" \
"&place_id=ChIJtfKDu-RkJA0ReHj0Ft_GUjE&ne_lat=41.14949817578736" \
"&ne_lng=-8.604029357647903&sw_lat=41.14179058380038&sw_lng" \
"=-8.615482054865367&zoom=16&search_by_map=true"

# para a madeira (funchal)
url_madeira = "https://www.airbnb.pt/s/Madeira--Funchal--Portugal/homes?tab_id=home_tab&refineme" \
"nt_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may" \
"&flexible_trip_lengths%5B%5D=weekend_trip" \
"&date_picker_type=calendar&query=Madeira%2C%20Funchal%2C%20Portugal" \
"&place_id=ChIJq4sfUMNfYAwROaHNFSxN2P8" \
              "&checkin=" + check_in + \
              "&checkout=" + check_out + \
              "&flexible_date_sea" \
"rch_filter_type=0&source=structured_search_input_header&search_type=autocomplete_click"


# ilha sao miguel - acores
url_sao_miguel = "https://www.airbnb.pt/s/São-Miguel--Açores/" \
                 "homes?tab_id=home_tab&refinement_paths" \
                 "%5B%5D=%2Fhomes&flexible_trip_dates" \
                 "%5B%5D=april&flexible_trip_dates" \
                 "%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=" \
                 "calendar" \
                 "&checkin=" + check_in + \
                 "&checkout=" + check_out + "&flexible_date_search_filter_type=0" \
                 "&source=structured_search_input_header&search_type" \
"=autocomplete_click&query=São%20Miguel%2C%20Açores&place_id=ChIJw5fmUHLXXAsRkDj2wyZvT64"


# vilamoura, algarve
url_vilamoura = "https://www.airbnb.pt/s/Vilamoura--Albufeira--Portugal/homes?" \
                "tab_id=home_tab&refinement_paths%5B%5D=%" \
                "2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%" \
                "5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip" \
                "&date_picker_type=calendar" \
                "&query=Vilamoura%2C%20Albufeira%2C%20Portugal&place" \
                "_id=ChIJ22D9y8a1Gg0RaSUQ3l8QguE" \
                "&checkin=" + check_in + \
                "&checkout=" + check_out + "&flexible_date_search_filter_type=0" \
                "&source=structured_search_input_header&search_type=autocomplete_click"

# lagos, algarve
url_lagos = "https://www.airbnb.pt/s/Lagos--Algarve--Portugal/homes?tab_id=home_tab" \
            "&refinement_paths%5B%5D=%2Fhomes" \
            "&flexible_trip_dates%5B%5D=april" \
            "&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip" \
            "&date_picker_type=calendar" \
            "&checkin=" + check_in + \
            "&checkout=" + check_out + "&flexible_date_search_filter_type=" \
            "0&source=structured_search_input_header&search_type=autocomplete_click&query=Lagos%2C%20Algarve%2C%20Portugal&place_id=ChIJjU0jUEkwGw0RV_waR6OqEFQ&federated_search_session_id" \
            "=adf02034-5f8a-4e6c-a222-0cdda987d725&pagination_search=true" \
            "&items_offset=20&section_offset=3"

# cascais
url_cascais = "https://www.airbnb.pt/s/" \
              "Cascais-e-Estoril--Cascais--Portugal/homes?tab_id=home_tab" \
              "&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&" \
              "flexible_trip_dates%5B%5D=may" \
              "&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar" \
              "&checkin=" + check_in + \
              "&checkout=" + check_out + \
              "&source=structured_search_input_header" \
              "&search_type=autocomplete_click&flexible_date_search_filter_type=0" \
              "&query=Cascais" \
              "%20e" \
              "%20Estoril%2C%20Cascais%2C%20Portugal&place_id=ChIJy6w4lnHEHg0RoEeQ5L3rAAU"

# sintra
url_sintra = "https://www.airbnb.pt/s/Sintra/homes?tab_id=home_tab&refinement_paths%5B%5D=%" \
             "2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may" \
             "&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar" \
             "&checkin=" + check_in + "&checkout=" + check_out + \
             "&source=structured_search_input" \
             "_header&search_type=autocomplete_click" \
             "&flexible_date_search_filter_type=0&query=Sintra" \
             "&place_id=ChIJ6Q5Rp8HaHg0RPFcPsMBcWBM"

# praia da nazare
url_nazare = "https://www.airbnb.pt/s/Nazaré--Portugal/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes" \
             "&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_lengths" \
             "%5B%5D=weekend_trip&date_picker_type=calendar&checkin=2022-04-06" \
             "&checkout=2022-04-07&flexible_date_search_filter_type=0" \
             "&source=structured_search_input_header" \
             "&search_type=autocomplete_click" \
             "&query=Nazaré%2C%20Portugal&place_id=ChIJ24D6dPGoGA0RIDaQ5L3rAAQ"
