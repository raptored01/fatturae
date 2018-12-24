# Generated by Django 2.1.4 on 2018-12-26 11:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('house_number', models.CharField(blank=True, max_length=20, verbose_name='House number')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='City')),
                ('province', models.CharField(blank=True, max_length=100, verbose_name='Province')),
                ('country_code', models.CharField(choices=[('AW', 'Aruba'), ('AF', 'Afghanistan'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AS', 'American Samoa'), ('AQ', 'Antarctica'), ('TF', 'French Southern Territories'), ('AG', 'Antigua and Barbuda'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BI', 'Burundi'), ('BE', 'Belgium'), ('BJ', 'Benin'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BF', 'Burkina Faso'), ('BD', 'Bangladesh'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BS', 'Bahamas'), ('BA', 'Bosnia and Herzegovina'), ('BL', 'Saint Barthélemy'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('BM', 'Bermuda'), ('BO', 'Bolivia, Plurinational State of'), ('BR', 'Brazil'), ('BB', 'Barbados'), ('BN', 'Brunei Darussalam'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('CF', 'Central African Republic'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CH', 'Switzerland'), ('CL', 'Chile'), ('CN', 'China'), ('CI', "Côte d'Ivoire"), ('CM', 'Cameroon'), ('CD', 'Congo, The Democratic Republic of the'), ('CG', 'Congo'), ('CK', 'Cook Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CV', 'Cabo Verde'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CX', 'Christmas Island'), ('KY', 'Cayman Islands'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DK', 'Denmark'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('ER', 'Eritrea'), ('EH', 'Western Sahara'), ('ES', 'Spain'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FR', 'France'), ('FO', 'Faroe Islands'), ('FM', 'Micronesia, Federated States of'), ('GA', 'Gabon'), ('GB', 'United Kingdom'), ('GE', 'Georgia'), ('GG', 'Guernsey'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GM', 'Gambia'), ('GW', 'Guinea-Bissau'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GD', 'Grenada'), ('GL', 'Greenland'), ('GT', 'Guatemala'), ('GF', 'French Guiana'), ('GU', 'Guam'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard Island and McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IM', 'Isle of Man'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IE', 'Ireland'), ('IR', 'Iran, Islamic Republic of'), ('IQ', 'Iraq'), ('IS', 'Iceland'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KN', 'Saint Kitts and Nevis'), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LC', 'Saint Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LS', 'Lesotho'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('MO', 'Macao'), ('MF', 'Saint Martin (French part)'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova, Republic of'), ('MG', 'Madagascar'), ('MV', 'Maldives'), ('MX', 'Mexico'), ('MH', 'Marshall Islands'), ('MK', 'Macedonia, Republic of'), ('ML', 'Mali'), ('MT', 'Malta'), ('MM', 'Myanmar'), ('ME', 'Montenegro'), ('MN', 'Mongolia'), ('MP', 'Northern Mariana Islands'), ('MZ', 'Mozambique'), ('MR', 'Mauritania'), ('MS', 'Montserrat'), ('MQ', 'Martinique'), ('MU', 'Mauritius'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('YT', 'Mayotte'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NU', 'Niue'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PA', 'Panama'), ('PN', 'Pitcairn'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PW', 'Palau'), ('PG', 'Papua New Guinea'), ('PL', 'Poland'), ('PR', 'Puerto Rico'), ('KP', "Korea, Democratic People's Republic of"), ('PT', 'Portugal'), ('PY', 'Paraguay'), ('PS', 'Palestine, State of'), ('PF', 'French Polynesia'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SD', 'Sudan'), ('SN', 'Senegal'), ('SG', 'Singapore'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJ', 'Svalbard and Jan Mayen'), ('SB', 'Solomon Islands'), ('SL', 'Sierra Leone'), ('SV', 'El Salvador'), ('SM', 'San Marino'), ('SO', 'Somalia'), ('PM', 'Saint Pierre and Miquelon'), ('RS', 'Serbia'), ('SS', 'South Sudan'), ('ST', 'Sao Tome and Principe'), ('SR', 'Suriname'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SE', 'Sweden'), ('SZ', 'Swaziland'), ('SX', 'Sint Maarten (Dutch part)'), ('SC', 'Seychelles'), ('SY', 'Syrian Arab Republic'), ('TC', 'Turks and Caicos Islands'), ('TD', 'Chad'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TM', 'Turkmenistan'), ('TL', 'Timor-Leste'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'Tanzania, United Republic of'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('US', 'United States'), ('UZ', 'Uzbekistan'), ('VA', 'Holy See (Vatican City State)'), ('VC', 'Saint Vincent and the Grenadines'), ('VE', 'Venezuela, Bolivarian Republic of'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('VN', 'Viet Nam'), ('VU', 'Vanuatu'), ('WF', 'Wallis and Futuna'), ('WS', 'Samoa'), ('YE', 'Yemen'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=2, verbose_name='Country Code')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('invoice_number', models.CharField(max_length=100, verbose_name='Invoice number')),
                ('transmission_format', models.CharField(choices=[('FPA12', 'FPA12'), ('FPR12', 'FPR12')], max_length=5, verbose_name='Transmission format')),
                ('recipient_code', models.CharField(max_length=7, verbose_name='Recipient code')),
                ('recipient_pec', models.EmailField(blank=True, max_length=254, verbose_name='Recipient PEC')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('country_code', models.CharField(choices=[('AW', 'Aruba'), ('AF', 'Afghanistan'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AS', 'American Samoa'), ('AQ', 'Antarctica'), ('TF', 'French Southern Territories'), ('AG', 'Antigua and Barbuda'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BI', 'Burundi'), ('BE', 'Belgium'), ('BJ', 'Benin'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BF', 'Burkina Faso'), ('BD', 'Bangladesh'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BS', 'Bahamas'), ('BA', 'Bosnia and Herzegovina'), ('BL', 'Saint Barthélemy'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('BM', 'Bermuda'), ('BO', 'Bolivia, Plurinational State of'), ('BR', 'Brazil'), ('BB', 'Barbados'), ('BN', 'Brunei Darussalam'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('CF', 'Central African Republic'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CH', 'Switzerland'), ('CL', 'Chile'), ('CN', 'China'), ('CI', "Côte d'Ivoire"), ('CM', 'Cameroon'), ('CD', 'Congo, The Democratic Republic of the'), ('CG', 'Congo'), ('CK', 'Cook Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CV', 'Cabo Verde'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CX', 'Christmas Island'), ('KY', 'Cayman Islands'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DK', 'Denmark'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('ER', 'Eritrea'), ('EH', 'Western Sahara'), ('ES', 'Spain'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FR', 'France'), ('FO', 'Faroe Islands'), ('FM', 'Micronesia, Federated States of'), ('GA', 'Gabon'), ('GB', 'United Kingdom'), ('GE', 'Georgia'), ('GG', 'Guernsey'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GM', 'Gambia'), ('GW', 'Guinea-Bissau'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GD', 'Grenada'), ('GL', 'Greenland'), ('GT', 'Guatemala'), ('GF', 'French Guiana'), ('GU', 'Guam'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard Island and McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IM', 'Isle of Man'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IE', 'Ireland'), ('IR', 'Iran, Islamic Republic of'), ('IQ', 'Iraq'), ('IS', 'Iceland'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KN', 'Saint Kitts and Nevis'), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LC', 'Saint Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LS', 'Lesotho'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('MO', 'Macao'), ('MF', 'Saint Martin (French part)'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova, Republic of'), ('MG', 'Madagascar'), ('MV', 'Maldives'), ('MX', 'Mexico'), ('MH', 'Marshall Islands'), ('MK', 'Macedonia, Republic of'), ('ML', 'Mali'), ('MT', 'Malta'), ('MM', 'Myanmar'), ('ME', 'Montenegro'), ('MN', 'Mongolia'), ('MP', 'Northern Mariana Islands'), ('MZ', 'Mozambique'), ('MR', 'Mauritania'), ('MS', 'Montserrat'), ('MQ', 'Martinique'), ('MU', 'Mauritius'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('YT', 'Mayotte'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NU', 'Niue'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PA', 'Panama'), ('PN', 'Pitcairn'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PW', 'Palau'), ('PG', 'Papua New Guinea'), ('PL', 'Poland'), ('PR', 'Puerto Rico'), ('KP', "Korea, Democratic People's Republic of"), ('PT', 'Portugal'), ('PY', 'Paraguay'), ('PS', 'Palestine, State of'), ('PF', 'French Polynesia'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SD', 'Sudan'), ('SN', 'Senegal'), ('SG', 'Singapore'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJ', 'Svalbard and Jan Mayen'), ('SB', 'Solomon Islands'), ('SL', 'Sierra Leone'), ('SV', 'El Salvador'), ('SM', 'San Marino'), ('SO', 'Somalia'), ('PM', 'Saint Pierre and Miquelon'), ('RS', 'Serbia'), ('SS', 'South Sudan'), ('ST', 'Sao Tome and Principe'), ('SR', 'Suriname'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SE', 'Sweden'), ('SZ', 'Swaziland'), ('SX', 'Sint Maarten (Dutch part)'), ('SC', 'Seychelles'), ('SY', 'Syrian Arab Republic'), ('TC', 'Turks and Caicos Islands'), ('TD', 'Chad'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TM', 'Turkmenistan'), ('TL', 'Timor-Leste'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'Tanzania, United Republic of'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('US', 'United States'), ('UZ', 'Uzbekistan'), ('VA', 'Holy See (Vatican City State)'), ('VC', 'Saint Vincent and the Grenadines'), ('VE', 'Venezuela, Bolivarian Republic of'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('VN', 'Viet Nam'), ('VU', 'Vanuatu'), ('WF', 'Wallis and Futuna'), ('WS', 'Samoa'), ('YE', 'Yemen'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=2, verbose_name='Country Code')),
                ('contact_phone', models.CharField(max_length=20, verbose_name='Contact Phone')),
                ('contact_email', models.CharField(max_length=200, verbose_name='Contact Email')),
                ('fiscal_code', models.CharField(max_length=16, verbose_name='Fiscal Code')),
                ('company_name', models.CharField(max_length=10, verbose_name='Company Name')),
                ('tax_regime', models.CharField(choices=[('RF01', 'Ordinario'), ('RF02', 'Contribuenti minimi (art.1, c.96-117, L. 244/07)'), ('RF03', 'Nuove iniziative produttive (art.13, L. 388/00) '), ('RF04', 'Agricoltura e attività connesse e pesca (artt.34 e 34-bis, DPR 633/72)'), ('RF05', 'Vendita sali e tabacchi (art.74, c.1, DPR. 633/72)'), ('RF06', 'Commercio fiammiferi (art.74, c.1, DPR 633/72)'), ('RF07', 'Editoria (art.74, c.1, DPR 633/72)'), ('RF08', 'Gestione servizi telefonia pubblica (art.74, c.1, DPR 633/72)'), ('RF09', 'Rivendita documenti di trasporto pubblico e di sosta (art.74, c.1, DPR 633/72)'), ('RF10', 'Intrattenimenti, giochi e altre attività di cui alla tariffa allegata al DPR 640/72 (art.74, c.6, DPR 633/72)'), ('RF11', 'Agenzie viaggi e turismo (art.74-ter, DPR 633/72) '), ('RF12', 'Agriturismo (art.5, c.2, L. 413/91)'), ('RF13', 'Vendite a domicilio (art.25-bis, c.6, DPR 600/73)'), ('RF14', 'Rivendita beni usati, oggetti d’arte, d’antiquariato o da collezione (art.36, DL 41/95)'), ('RF15', 'Agenzie di vendite all’asta di oggetti d’arte, antiquariato o da collezione (art.40-bis, DL 41/95)'), ('RF16', 'IVA per cassa P.A. (art.6, c.5, DPR 633/72)'), ('RF17', 'IVA per cassa (art. 32-bis, DL 83/2012)'), ('RF18', 'Altro'), ('RF19', 'Regime forfettario (art.1, c.54-89, L. 190/2014)')], max_length=4, verbose_name='Tax Regime')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='invoices.Address', verbose_name='Address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
