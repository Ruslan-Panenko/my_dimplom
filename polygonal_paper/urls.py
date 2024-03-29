from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from sale import views
from shop.models import item, subcategory


def main(request):
    cat = 10
    for i in item.objects.filter(category=cat):
        print(f'["{i.title}", "{i.slug}", {i.price}, "{i.main_photo_xxl2}"],')
    print(item.objects.filter(category=cat).first())
    return 0


def func(request):
    cat = subcategory.objects.get(id=9)
    try:
        for c in cup:
            new_cup = item()
            new_cup.title = c[0]
            new_cup.slug = c[1]
            new_cup.price = c[2]
            new_cup.main_photo_xxl2 = c[3]
            new_cup.category = cat
            new_cup.order = 1
            new_cup.save()
    except:
        print(1)
    mod = subcategory.objects.get(id=8)
    
    try:
        for m in model:
            new_cup = item()
            new_cup.title = m[0]
            new_cup.slug = m[1]
            new_cup.price = m[2]
            new_cup.main_photo_xxl2 = m[3]
            new_cup.category = mod
            new_cup.order = 1
            new_cup.save()
    except:
        print(1)

    mod_br = subcategory.objects.get(id=7)
    
    try:
        for b in brelk:
            new_cup = item()
            new_cup.title = b[0]
            new_cup.slug = b[1]
            new_cup.price = b[2]
            new_cup.main_photo_xxl2 = b[3]
            new_cup.category = mod_br
            new_cup.order = 1
            new_cup.save()
    except:
        print(1)

    mod_chair = subcategory.objects.get(id=6)
    
    try:
        for c in chairs:
            new_cup = item()
            new_cup.title = c[0]
            new_cup.slug = c[1]
            new_cup.price = c[2]
            new_cup.main_photo_xxl2 = c[3]
            new_cup.category = mod_chair
            new_cup.order = 1
            new_cup.save()
    except:
        print(1)

    mod_tab = subcategory.objects.get(id=5)
    
    try:
        for t in tables:
            new_cup = item()
            new_cup.title = t[0]
            new_cup.slug = t[1]
            new_cup.price = t[2]
            new_cup.main_photo_xxl2 = t[3]
            new_cup.category = mod_tab
            new_cup.order = 1
            new_cup.save()
    except:
        print(1)

    mod_mon = subcategory.objects.get(id=4)
    
    try:
        for m in monitor:
            new_cup = item()
            new_cup.title = m[0]
            new_cup.slug = m[1]
            new_cup.price = m[2]
            new_cup.main_photo_xxl2 = m[3]
            new_cup.category = mod_mon
            new_cup.order = 1
            new_cup.save()
    except:
        print(1)

    mod_h = subcategory.objects.get(id=3)
    
    try:
        for h in headphones:
            new_cup = item()
            new_cup.title = h[0]
            new_cup.slug = h[1]
            new_cup.price = h[2]
            new_cup.main_photo_xxl2 = h[3]
            new_cup.category = mod_h
            new_cup.order = 1
            new_cup.save()
    except:
        print(1)

    mod_m = subcategory.objects.get(id=1)
    
    try:
        for m in mouses:
            new_cup = item()
            new_cup.title = m[0]
            new_cup.slug = m[1]
            new_cup.price = m[2]
            new_cup.main_photo_xxl2 = m[3]
            new_cup.category = mod_m
            new_cup.order = 1
            new_cup.save()
    except:
        print(1)


        mod_k = subcategory.objects.get(id=2)
    
    try:
        for k in keyboards:
            new_cup = item()
            new_cup.title = k[0]
            new_cup.slug = k[1]
            new_cup.price = k[2]
            new_cup.main_photo_xxl2 = k[3]
            new_cup.category = mod_k
            new_cup.order = 1
            new_cup.save()
    except:
        print(1)
    return 0

urlpatterns = [
                  path('about/', views.about),
                  path('zxc/', func),
                  path('delivery/', views.delivery),
                  path('contact/', views.contact),

                  path('admin/', admin.site.urls),
                  path('cart/', include('cart.urls', namespace='cart')),
                  path('coupons/', include('sale.urls', namespace='coupons')),
                  path('order/', include('order.urls', namespace='order')),

                  path('', include('shop.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

cup = [["ABYstyle Harry Potter (ABYMUG521)", "747f8b9e-f268-4038-8fe8-71075ded8cf3", 599,
        "https://www.3ona51.com/images/products/cups_/abystyle-harry-potter-abymug521/250.jpg"],
       ["ABYstyle Harry Potter 460ml (ABYMUG301)", "52a8eb26-489a-4fd3-9999-3cffc8462e9b", 499,
        "https://www.3ona51.com/images/products/cups_/abystyle-harry-potter-460ml-abymug301/250.jpg"],
       ["Blizzard World of Warcraft: Battle for Azeroth Stein (B63241)", "90c6bd4a-84b9-474a-94a8-eef82df2883d", 2269,
        "https://www.3ona51.com/images/products/cups_/blizzard-world-of-warcraft-battle-for-azeroth-stein-b63241/250.jpg"],
       ["ABYstyle DC Comics Superman (ABYMUG446)", "047a8468-42b6-457a-ad2e-72974e1e5a24", 499,
        "https://www.3ona51.com/images/products/cups_/abystyle-dc-comics-superman-abymug446/250.jpg"],
       ["ABYstyle Assassin's Creed (ABYMUG417)", "cfcc8c03-ba5e-4ce8-a70b-61798372070e", 499,
        "https://www.3ona51.com/images/products/cups_/abystyle-assassin-s-creed-abymug417/250.jpg"],
       ["ABYstyle DC Comics  Batman & Joker (ABYMUG382)", "09df0595-0b78-4a4d-a129-c09ed3aa97e3", 499,
        "https://www.3ona51.com/images/products/cups_/abystyle-dc-comics-batman-joker-abymug382/250.jpg"],
       ["Abystyle DC COMICS BATMAN (ABYMUG363)", "6f84e781-90e7-4564-9c99-200229fc2f03", 599,
        "https://www.3ona51.com/images/products/cups_/abystyle-dc-comics-batman-abymug363/250.jpg"],
       ["ABYstyle Halo (ABYMUG242)", "a221f2d3-111f-4cee-b7a8-3b055060e516", 599,
        "https://www.3ona51.com/images/products/cups_/abystyle-halo-abymug242/250.jpg"]]

model = [["Blizzard Overwatch Genji Statue (B62464)", "e5d557c2-6410-4ae7-820f-850b68ee818a", 6999,
          "https://www.3ona51.com/images/products/models/blizzard-overwatch-genji-statue-b62464/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Reinhardt Figure (B63060)", "90dcc33d-365b-4a72-8df2-54c1108dfa01",
          599,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--reinhardt-figure-b63060/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Winston (B62943)", "b1d5979c-e988-4ccb-a1fb-cc04aecc1d63", 599,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--winston-b62943/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Vampire Symmetra Figure (B63064)",
          "ac0a381a-0300-4832-aed6-fb3a02107e42", 399,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--vampire-symmetra-figure-b63064/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Nuit Widowmaker (B63525)", "83f50a4b-d8ea-4348-81ca-e816481a40d9",
          399,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--nuit-widowmaker-b63525/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Shiver Reaper Figure (B63068)",
          "4454ac92-9378-47c3-b75a-fb3c19babf46", 399,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--shiver-reaper-figure-b63068/250.jpg"],
         ["Blizzard Overwatch Mercy Statue (B62908)", "b4da64ec-ac52-4d9b-b91a-74580f05d116", 6999,
          "https://www.3ona51.com/images/products/models/blizzard-overwatch-mercy-statue-b62908/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Peppermint Sombra Figure (B63069)",
          "82ce0475-1ae8-4786-afb9-34ac395177d7", 399,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--peppermint-sombra-figure-b63069/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Series 4 (B62928)", "89f5d8fb-912b-48fd-aacd-2c99aa719f33", 249,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--series-4-b62928/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Series 3 (Overwatch Edition) (B62457)",
          "4f05aa8d-1efa-41d4-b2ac-0a0daeca6a95", 249,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--series-3-overwatch-edition-b62457/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Demon Hanzo Figure (B63065)", "0abd5b94-304b-425d-88e8-32c4ba8276cd",
          399,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--demon-hanzo-figure-b63065/250.jpg"],
         ["Blizzard Cute But Deadly Blind Vinyls - Frosted Zarya Figure (B63067)",
          "0125e2dd-54ef-4ea4-b55d-475db9bbc970", 399,
          "https://www.3ona51.com/images/products/models/blizzard-cute-but-deadly-blind-vinyls--frosted-zarya-figure-b63067/250.jpg"],
         ["The Witcher 3: Wild Hunt: Geralt in Bath (761568003505)", "e8dee531-fdb4-40be-b2d7-57a2eee75baf", 2949,
          "https://www.3ona51.com/images/products/models/the-witcher-3-wild-hunt-geralt-in-bath-761568003505/250.jpg"],
         ["Blizzard World of Warcraft Saurfang (B63210)", "e4180c34-17a9-4f9d-a6ac-8e324ab2997b", 1999,
          "https://www.3ona51.com/images/products/models/blizzard-world-of-warcraft-saurfang-b63210/250.jpg"],
         ["The Witcher 3: Wild Hunt: Ciri (761568000269)", "93478ce0-544b-4f16-a3cc-70c116d36c4a", 1649,
          "https://www.3ona51.com/images/products/models/the-witcher-3-wild-hunt-ciri-761568000269/250.jpg"],
         ["The Witcher 3: Wild Hunt: Ciri 2nd Edition (761568005288)", "19c8955d-2201-47dc-a43e-2ac42075d6ce", 1899,
          "https://www.3ona51.com/images/products/models/the-witcher-3-wild-hunt-ciri-2nd-edition-761568005288/250.jpg"],
         ["The Witcher 3: Wild Hunt: Geralt Grandmaster Feline (761568005042)", "d85da69c-5e45-4b52-9c61-4bc3bfe5ba1c",
          1899,
          "https://www.3ona51.com/images/products/models/the-witcher-3-wild-hunt-geralt-grandmaster-feline-761568005042/250.jpg"],
         ["The Witcher 3: Wild Hunt: Regis The Vampire Deluxe (761568005578)", "cf2840b7-ec09-40b2-ad25-ddaac97ddb89",
          2149,
          "https://www.3ona51.com/images/products/models/the-witcher-3-wild-hunt-regis-the-vampire-deluxe-761568005578/250.jpg"],
         ["The Witcher 3: Wild Hunt: Yennefer 2nd Edition (761568005295)", "04bf75a8-075e-456b-82ea-0fccc7a68ae8", 1899,
          "https://www.3ona51.com/images/products/models/the-witcher-3-wild-hunt-yennefer-2nd-edition-761568005295/250.jpg"],
         ["The Witcher 3: Wild Hunt: Dandelion (761568001761)", "277402b2-e7b5-4ca9-93b5-a57ffc7a0f9a", 1649,
          "https://www.3ona51.com/images/products/models/the-witcher-3-wild-hunt-dandelion-761568001761/250.jpg"]]

brelk = [["ABYstyle Assassin's Creed (ABYKEY012)", "968e1d8d-deea-47f1-ab00-e02a64f2b97b", 249,
          "https://www.3ona51.com/images/products/keychains_/abystyle-assassin-s-creed-abykey012/250.jpg"],
         ["ABYstyle The Walking Dead (ABYKEY205)", "1b1aa14d-dab2-4a9c-b9ef-480e8343f25d", 299,
          "https://www.3ona51.com/images/products/keychains_/abystyle-the-walking-dead-abykey205/250.jpg"],
         ["ABYstyle Far Cry Croix (ABYKEY248)", "1f2f5aea-739f-4b99-8ea6-4f897b87ff7d", 249,
          "https://www.3ona51.com/images/products/keychains_/abystyle-far-cry-croix-abykey248/250.jpg"],
         ["ABYstyle Overwatch D.VA (ABYKEY215)", "5d9be7a6-81a2-438f-9a57-39dd749d198e", 199,
          "https://www.3ona51.com/images/products/keychains_/abystyle-overwatch-d-va-abykey215/250.jpg"],
         ["ABYstyle Overwatch Blackwatch (ABYKEY264)", "d4308101-d2b6-42be-b47c-559a78bb3501", 249,
          "https://www.3ona51.com/images/products/keychains_/abystyle-overwatch-blackwatch-abykey264/250.jpg"],
         ["ABYstyle DC Comics Logo Superman (ABYKEY054)", "98f60d5b-53e4-4b8e-83e0-94bd728356ce", 199,
          "https://www.3ona51.com/images/products/keychains_/abystyle-dc-comics-logo-superman-abykey054/250.jpg"],
         ["ABYstyle Harry Potter (ABYKEY192)", "d467e1c1-3889-4924-a725-635c39de9795", 249,
          "https://www.3ona51.com/images/products/keychains_/abystyle-harry-potter-abykey192/250.jpg"],
         ["ABYstyle Assassin's Creed (ABYKEY249)", "1ef53465-6b7c-485a-928d-9defe3241702", 249,
          "https://www.3ona51.com/images/products/keychains_/abystyle-assassin-s-creed-abykey249/250.jpg"],
         ["ABYstyle Overwatch (ABYKEY170)", "3a866b3d-be05-425e-bbca-8de19aa9c4f3", 199,
          "https://www.3ona51.com/images/products/keychains_/abystyle-overwatch-abykey170/250.jpg"],
         ["ABYstyle Rick and Morty Pickle Rick (ABYKEY252)", "a4c20446-6d1a-4e89-af94-12bebcb639f0", 249,
          "https://www.3ona51.com/images/products/keychains_/abystyle-rick-and-morty-pickle-rick-abykey252/250.jpg"],
         ["ABYstyle Assassin's Creed (ABYKEY080)", "dc4a6c71-08a1-483b-aaa7-da5879530a71", 249,
          "https://www.3ona51.com/images/products/keychains_/abystyle-assassin-s-creed-abykey080/250.jpg"],
         ["ABYstyle Heathstone Rosace (ABYKEY200)", "dad2c9e0-a40c-4ac5-b34c-4179e9a9237d", 299,
          "https://www.3ona51.com/images/products/keychains_/abystyle-heathstone-rosace-abykey200/250.jpg"],
         ["ABYstyle DC Comics Logo Batman (ABYKEY053)", "0fd12e35-052d-4a21-9708-c1cf0af28a63", 249,
          "https://www.3ona51.com/images/products/keychains_/abystyle-dc-comics-logo-batman-abykey053/250.jpg"],
         ["ABYstyle DC Comics Logo Wonder Woman (ABYKEY171)", "646fbf57-e65c-405f-ad87-1c468e9b10c2", 249,
          "https://www.3ona51.com/images/products/keychains_/abystyle-dc-comics-logo-wonder-woman-abykey171/250.jpg"],
         ["ABYstyle DC Comics (ABYKEY167)", "f4af0433-1d41-4656-ab4d-62f496ee1c70", 449,
          "https://www.3ona51.com/images/products/keychains_/abystyle-dc-comics-abykey167/250.jpg"],
         ["Rick & Morty - Pickled Rick 3D Rubber Keychain (KE851414RMT)", "c94dc6e2-3eb5-4f8b-aabe-2a545c803536", 339,
          "https://www.3ona51.com/images/products/keychains_/rick-morty--pickled-rick-3d-rubber-keychain-ke851414rmt/250.jpg"],
         ["Adventure Time - Sitting Finn Rubber Keychain (KE260329ADV)", "17dffc37-10f7-4c59-95e3-405a9e64d806", 139,
          "https://www.3ona51.com/images/products/keychain/adventure-time-sitting-finn-rubber-keychain-ke260329adv/250.jpg"],
         ["Fallout - 3D Metal Keychain (KE255707FAL)", "dfe58608-2683-4a24-8619-1cea0b9e6a88", 339,
          "https://www.3ona51.com/images/products/keychains_/fallout--3d-metal-keychain-ke255707fal/250.jpg"],
         ["Assassin's Creed Odyssey - Odyssey Logo Metal Keychain (KE234321ACO)",
          "a390c2ac-d729-4680-b7b8-99a362df8c4b", 239,
          "https://www.3ona51.com/images/products/keychain/assassins-creed-odyssey-odysse-logo-metal-keychain-ke234321aco/250.jpg"],
         ["Adventure Time - Lumpy Space Princess Rubber Keychain (KE260330ADV)", "ef8b2106-4a26-44f3-80cf-d02aba0b978d",
          175,
          "https://www.3ona51.com/images/products/keychain/adventure-time-lumpy-space-princess-rubber-keychain-ke260330adv/250.jpg"]]

chairs = [["Hator Darkside (HTC-919) Black", "ef09ef47-4a67-4af1-b755-2dd546032f90", 7199,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-darkside-htc-919-black/250.jpg"],
          ["Hator Arc (HTC-985) Phantom Black", "208adbcb-811c-494d-a0f9-b7ae4450a6e6", 14499,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-htc-985-phantom-black/250.jpg"],
          ["DXRacer G Series D8200 GC-G001-NR-B2-NVF Black/Red", "f0815df9-e3dd-404d-b4ea-12bd4834a1c8", 10999,
           "https://www.3ona51.com/images/products/gaming-chairs/dxracer-g-series-d8200-gc-g001-nr-b2-nvf-black-red/250.jpg"],
          ["Hator Arc (HTC-986) Terracotta", "94b7dc45-d544-4844-8155-2dc266ccf6ca", 13499,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-htc-986-terracotta/250.jpg"],
          ["DXRacer Air PRO AIR/D7200/N Black", "e4a6aa71-7386-40a9-8a53-02b1f56437e4", 15999,
           "https://www.3ona51.com/images/products/gaming-chairs/dxracer-a-series-oa-ch001-n-2-nvf-black/250.jpg"],
          ["DXRacer King GC-K99-N-A3-01-NVF Black", "3b136f78-62a5-4eb2-a3ad-f80599e44aee", 14999,
           "https://www.3ona51.com/images/products/gaming-chairs/dxracer-king-gc-k99-n-a3-01-nvf-black/250.jpg"],
          ["Hator Arc Fabric (HTC-997) Emerald", "7535dcde-6638-4f9f-bfb2-38d06b7ad010", 17999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-fabric-htc-997-emerald/250.jpg"],
          ["DXRacer Air PRO AIR/D7200/WRB.G Yellow & Red & Blue", "dbe5f13f-956e-49fb-ae45-0642e4ff4ec3", 15999,
           "https://www.3ona51.com/images/products/gaming-chairs/dxracer-air-pro-air-d7200-wrb-g-yellow-red-blue/250.jpg"],
          ["Razer Iskur Black (RZ38-02770200-R3G1)", "651e7be4-6936-41ff-98b7-21111a7fe02a", 16999,
           "https://www.3ona51.com/images/products/gaming-chairs/razer-iskur-black-rz38-02770200-r3g1/250.jpg"],
          ["DXRacer King GC-K99-NG-A3-01-NVF Grey", "04ca4f4c-d2e4-48b0-bbca-808938ed1858", 14999,
           "https://www.3ona51.com/images/products/gaming-chairs/dxracer-king-gc-k99-ng-a3-01-nvf-grey/250.jpg"],
          ["Hator Arc S (HTC-1004) Phantom Black", "70ea9c80-75bb-4585-babd-3633c0f74e5c", 18999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-s-htc-1004-phantom_black/250.jpg"],
          ["Hator Arc Fabric (HTC-996) Sandy Brown", "5dd58f92-adc3-4b90-b2f4-6ee763a7aa13", 13999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-fabric-htc-996-sandy-brown/250.jpg"],
          ["Hator Arc Fabric (HTC-993) Plummy Violet", "cb4dcf7b-d1ae-4e28-94d6-d61fdcd562f9", 13999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-fabric-htc-993-plummy-violet/250.jpg"],
          ["Hator Arc Fabric (HTC-980) Sweety Mint", "a7106b0c-2ddb-4665-81b9-a5576a00ce46", 13999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-fabric-htc-980-sweety-mint/250.jpg"],
          ["Hator Arc Fabric (HTC-981) Juicy Lime", "c344352c-528f-4842-9b77-3abd73844ab4", 13999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-fabric-htc-981-juicy-_lime/250.jpg"],
          ["Hator Arc S (HTC-1000) Marrakesh Brown", "eb826b4b-a0f4-4c49-8221-4001a384692f", 18999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-s-htc-1000-marrakesh-brown/250.jpg"],
          ["DXRacer Air PRO AIR/D7200/WRN.G White / Red", "d5adbfae-990d-4276-9bcc-dcc120e48ab7", 15999,
           "https://www.3ona51.com/images/products/gaming-chairs/dxracer-air-pro-air-d7200-wrn-g-white-red/250.jpg"],
          ["Hator Arc Fabric (HTC-995) Saffron Yellow", "ad3ac512-2b19-41e2-a19c-fa3d5311c687", 13999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-fabric-htc-995-saffron-yellow/250.jpg"],
          ["Hator Arc S (HTC-1001) Mineral Grey", "0d880267-6327-444d-aba0-37022d023764", 18999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-s-htc-1001-mineral-grey/250.jpg"],
          ["Hator Arc Fabric (HTC-994) Stelvio Red", "c7e848e0-b3aa-4511-a166-f30abb3a0933", 13999,
           "https://www.3ona51.com/images/products/gaming-chairs/hator-arc-fabric-htc-994-stelvio-red/250.jpg"]]

tables = [["HATOR Vast Essential Black (HTD-010)", "6de433f6-fe19-4689-90fa-30c30a040b73", 4999,
           "https://www.3ona51.com/images/products/gaming-desks/hator-vast-essential-black-htd-010/250.jpg"],
          ["HATOR Vast PRO Black (HTD-050)", "1bc3bf2a-edb3-42b7-8c42-f4cb37351f5f", 9999,
           "https://www.3ona51.com/images/products/gaming-desks/hator-vast-pro-black-htd-050/250_8.jpg"],
          ["DXRacer GD/003/N Black", "f7a7bbcd-4247-48c8-986e-f4cbe017ff54", 7999,
           "https://www.3ona51.com/images/products/gaming-desks/dxracer-gd-003-n-black/250.jpg"],
          ["HATOR Vast Essential Wallnut/White (HTD-011)", "036682ff-47a3-4789-8765-52581b386178", 4999,
           "https://www.3ona51.com/images/products/gaming-desks/hator-vast-essential-wallnut-white-htd-011/250.jpg"],
          ["DXRacer LT/007/N Black", "b74f4510-6493-40e9-aad6-1819ed599abb", 5999,
           "https://www.3ona51.com/images/products/gaming-desks/dxracer-lt-007-n-black/250.jpg"],
          ["HATOR Vast Essential White (HTD-012)", "3b666e47-ba8a-4ec1-ba60-69016962d27a", 4999,
           "https://www.3ona51.com/images/products/gaming-desks/hator-vast-essential-white-htd_012/250.jpg"],
          ["HATOR Vast PRO Wallnut/White (HTD-051)", "ab6d2039-7530-4797-89ae-06763c8a54ea", 9999,
           "https://www.3ona51.com/images/products/gaming-desks/hator-vast-pro-wallnut-white-htd-051/250.jpg"],
          ["HATOR Vast PRO White (HTD-052)", "f1f601eb-b159-43c9-b895-57c188fff229", 9999,
           "https://www.3ona51.com/images/products/gaming-desks/hator-vast-pro-white-htd-052/250.jpg"]]

monitor = [["Asus ROG Strix 43 XG43UQ (90LM0590-B02170)", "2e70345c-b8e8-4c51-8ccf-79d3ce5fe4a2", 66599,
            "https://www.3ona51.com/images/products/monitors/asus-rog-strix-43-xg43uq-90lm0590-b02170/250.jpg"],
           ["HyperX Armada 27 (64V69AA)", "6b75ce0a-931b-416e-ad78-1c5259a640b8", 22499,
            "https://www.3ona51.com/images/products/monitors/hyperx-armada-27-64v69aa/250.jpg"],
           ["HyperX Armada 25 (64V61AA)", "e3095f0a-810d-4b68-be99-a1ce5511660c", 19999,
            "https://www.3ona51.com/images/products/monitors/hyperx-armada-25-xg43uq-64v61aa/250.jpg"],
           ["Asus TUF Gaming 34 VG34VQEL1A (90LM06F0-B01E70)", "8961ae9a-f0aa-496b-9245-553f84d4cc42", 22999,
            "https://www.3ona51.com/images/products/monitors/asus-tuf-gaming-34-vg34vqel1a-90lm06f0-b01e70/250.jpg"],
           ["Asus 42.5 XG438QR (90LM04U0-B02170)", "1faf5f0a-e3fe-4fa8-a9f5-0b07c8466031", 55599,
            "https://www.3ona51.com/images/products/monitors/asus-42-5-xg438qr-90lm04u0-b02170/250.jpg"],
           ["Asus ROG Swift 32 PG329Q-W (90LM06L2-B01170)", "7802b3c8-1baa-45ac-b9df-c58fc9c314ad", 41699,
            "https://www.3ona51.com/images/products/monitors/asus-rog-swift-32-pg329q-w-90lm06l2-b01170/250.jpg"],
           ["Asus TUF Gaming 27 VG27AQA1A (90LM05Z0-B05370)", "8d68890a-eae7-4ed4-823c-a4bf2d8d4074", 13999,
            "https://www.3ona51.com/images/products/monitors/asus-tuf-gaming-27-vg27aqa1a-90lm05z0-b05370/250.jpg"],
           ["Asus TUF Gaming 27 VG279Q1R (90LM05S1-B01E70)", "74f009e4-50b0-4a03-9630-7029eb1b9c9b", 10999,
            "https://www.3ona51.com/images/products/monitors/asus-tuf-gaming-27-vg279q1r-90lm05s1-b01e70/250.jpg"],
           ["Asus 32 VG32VQR (90LM04I0-B03170)", "a7bc79d1-2a51-4a29-bb84-933050b5c397", 16599,
            "https://www.3ona51.com/images/products/monitors/asus-32-vg32vqr-90lm04i0-b03170/250.jpg"]]

headphones = [["Hator Hypergang EVO (HTA-810)", "41fed3d0-59ae-460e-b5fd-c1fbc7bab448", 1699,
               "https://www.3ona51.com/images/products/gaming-headphones/hator-hypergang-evo_hta-810/250.jpg"],
              ["Logitech Wireless Gaming Combo (981-001162)", "b53b9dce-1071-4d4c-b209-bae4b49451ae", 3599,
               "https://www.3ona51.com/images/products/gaming-headphones/igrovoj-komplekt-logitech-wireless-gaming-combo-981-001162/250.jpg"],
              ["Logitech G Pro X Gaming Headset (981-000818)", "fbcb8263-2da5-4484-bd56-17ca21cd7593", 4799,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-g-pro-x-gaming-headset-981-000818/250.jpg"],
              ["Razer Blackshark V2 X (RZ04-03240100-R3M1)", "a58b177a-8793-4d5a-a6a5-2c0ce0cea7a0", 2299,
               "https://www.3ona51.com/images/products/gaming-headphones/razer-blackshark-v2-x-rz04-03240100-r3m1/250.jpg"],
              ["Hator Hypergang EVO Elite (HTA-830) Black", "9f08a00a-c1b1-40d4-8269-364156831c1f", 1999,
               "https://www.3ona51.com/images/products/gaming-headphones/hator-hypergang-evo-elite-hta_830-black/250.jpg"],
              ["Hator Hypergang Wireless Tri-mode Black (HTA-850)", "41cd33ec-0f9d-4914-a264-9aa286d3f2c8", 2999,
               "https://www.3ona51.com/images/products/gaming-headphones/hator-hypergang-wireless-tri-mode-black-hta-850/250.jpg"],
              ["Razer Kraken Green (RZ04-02830200-R3M1)", "0dc15a1b-4c04-4937-963f-ba9955eb4e1e", 2499,
               "https://www.3ona51.com/images/products/razer/kraken-multi-platform-green-rz04-02830200-r3m1/250.jpg"],
              ["Razer Kraken Black (RZ04-02830100-R3M1)", "3b7ac718-de51-4a9d-b398-a2eaa5df45eb", 2299,
               "https://www.3ona51.com/images/products/gaming-headphones/razer-kraken-multi-platform-black-rz04-02830100-r3m1/250.jpg"],
              ["Hator Hellraizer (HTA-814) White", "e33d75d8-a5f4-4581-bce9-0b524e0d314f", 899,
               "https://www.3ona51.com/images/products/gaming-headphones/hator-hellraizer-hta-814-white/250.jpg"],
              ["Logitech G435 Black (981-001050)", "59ce89a2-ccdf-4657-ae3c-7cc27d855fa7", 3399,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-g435-black-981-001050/250.jpg"],
              ["Razer Blackshark V2 X White (RZ04-03240700-R3M1)", "cfd56bbc-55d6-4509-b051-39df03c61c60", 2299,
               "https://www.3ona51.com/images/products/gaming-headphones/razer-blackshark-v2-x-white-rz04-03240700-r3m1/250_5.jpg"],
              ["Logitech G Pro Gaming Headset (981-000812)", "dc534d64-ae5e-4382-a086-41923eaa68b5", 3999,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-g-pro-gaming-headset-981-000812/250.jpg"],
              ["Logitech G335 Wired Gaming Headset Black (981-000978)", "2454e78e-5731-4c59-8777-4874ee3ec2f8", 2799,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-g335-wired-gaming-headset-white-981-001018/250.jpg"],
              ["Logitech G335 Wired Gaming Headset White (981-001018)", "841fc6a6-7708-4a6f-b0c0-78d2ce177d29", 2599,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-g335-wired-gaming-headset-white-981-001018/250_3.jpg"],
              ["Logitech G435 White (981-001074)", "0a5ceb79-8f5c-46f3-95ee-6543e8b6a0d9", 3199,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-g435-white-981-001074/250.jpg"],
              ["Razer Barracuda X 2022 Black (RZ04-04430100-R3M1)", "9a0b482c-27bf-467f-ac67-19e85f8adceb", 3999,
               "https://www.3ona51.com/images/products/gaming-headphones/razer-barracuda-x-2022-black-rz04-04430100-r3m1/250.jpg"],
              ["Logitech FITS True Wireless Gaming Earbuds Black (985-001182)", "ccb5149e-9c1e-4b72-a1ab-5c619bd91ea1",
               6999,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-fits-true-wireless-gaming-earbuds-black-985-001182/250.jpg"],
              ["Logitech G435 Blue (981-001062)", "2b5ed43e-b68c-4a47-9d88-f48cc0a347c0", 2999,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-g435-blue-981-001062/250.jpg"],
              ["Logitech FITS True Wireless Gaming Earbuds White (985-001183)", "694cd1c1-4650-46de-9e5b-765741198285",
               6999,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-fits-true-wireless-gaming-earbuds-white-985-001183/250.jpg"],
              ["Logitech G335 Wired Gaming Headset Mint (981-001024)", "8beca817-994d-44fb-8d41-834c59be4dca", 2599,
               "https://www.3ona51.com/images/products/gaming-headphones/logitech-g335-wired-gaming-headset-mint-981-001024/250.jpg"]]

mouses = [["ASUS ROG Gladius III AimPoint RGB White (90MP02Y0-BMUA10)", "5ae418c6-0f0e-4557-a0e3-de223539c956", 4549,
           "https://www.3ona51.com/images/products/gaming-mouses/asus-rog-gladius-iii-aimpoint-rgb-white-90mp02y0-bmua10/250.jpg"],
          ["Razer DeathAdder Essential (RZ01-03850100-R3M1)", "b0e80989-f068-46a5-b805-dd505c4f787a", 949,
           "https://www.3ona51.com/images/products/gaming-mouses/razer-deathadder-essential-rz01-02540100-r3m1/250_6.jpg"],
          ["Logitech G PRO X Superlight Wireless Black (910-005880)", "e031ca5e-69eb-4f42-8d4a-178d44faa8c5", 5699,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g-pro-x-superlight-wireless-black-910-005880/250.jpg"],
          ["Razer DeathAdder V2 (RZ01-03210100-R3M1)", "c2e7ad53-e9f5-4b71-b565-5e67b5747c7d", 1699,
           "https://www.3ona51.com/images/products/gaming-mouses/razer-deathadder-v2-rz01-03210100-r3m1/250.jpg"],
          ["Razer Basilisk X Hyperspeed (RZ01-03150100-R3G1)", "65b823bb-1783-4e2d-b98a-1419ecb71d19", 1799,
           "https://www.3ona51.com/images/products/gaming-mouses/razer-basilisk-x-hyperspeed-rz01-03150100-r3g1/250.jpg"],
          ["Hator Quasar Wireless Black (HTM-420)", "04a0f489-fd56-4d73-9456-27bd36e2d799", 1799,
           "https://www.3ona51.com/images/products/gaming-mouses/hator-quasar-wireless-black-htm-420/250.jpg"],
          ["Razer Viper Ultimate & Mouse Dock (RZ01-03050100-R3G1)", "f3b1ac9f-e6ca-45ce-ad53-6e0da909bbd7", 4499,
           "https://www.3ona51.com/images/products/gaming-mouses/razer-viper-ultimate-rz01-03050100-r3g1/250.jpg"],
          ["Hator Pulsar Essential (HTM-312)", "bf121f05-ad0e-4c55-aec4-084f4d524091", 799,
           "https://www.3ona51.com/images/products/gaming-mouses/hator-pulsar-essential-htm_312/250.jpg"],
          ["Logitech G PRO X Superlight Wireless Magenta (910-005956)", "3d0c863e-0df3-43ae-be7b-efad5baf0495", 5499,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g-pro-x-superlight-wireless-magenta-910-005956/250.jpg"],
          ["Logitech G102 Lightsync Black (910-005823)", "657c10a1-42b1-4c51-90a8-b17ca9f570b4", 999,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g102-lightsync-black-910-005823/250.jpg"],
          ["Logitech G PRO Wireless (910-005272)", "035fe31a-b108-478c-be8d-ed895cbc5851", 4799,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g-pro-wireless-910_005272/250.jpg"],
          ["Logitech G PRO X Superlight Wireless White (910-005942)", "f280348a-e129-44a1-a289-151381ed3c6f", 5499,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g-pro-x-superlight-wireless-white-910-005942/250.jpg"],
          ["Hator Pulsar Wireless White (HTM-316)", "04f6b705-8bcb-4617-bb60-d0adede7febd", 1499,
           "https://www.3ona51.com/images/products/gaming-mouses/hator-pulsar-wireless-white-htm-316/250.jpg"],
          ["Logitech G102 Lightsync White (910-005824)", "974f1e98-0ce8-4274-ba02-18efaa8e9fa1", 999,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g102-lightsync-white-910-005824/250.jpg"],
          ["Hator Pulsar Wireless Black (HTM-315)", "888b9c85-1ef2-446a-a0fc-8653c178315f", 1499,
           "https://www.3ona51.com/images/products/gaming-mouses/hator-pulsar-wireless-black-htm-315/250.jpg"],
          ["Logitech G102 Lightsync Lilac (910-005854)", "e8aa3568-89e1-4495-97a5-944f0b6bb463", 999,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g102-lightsync-lilac-910-005854/250.jpg"],
          ["Logitech G305 Lightspeed Wireless Black (910-005282)", "7948f619-0037-4125-9cf6-52371d976766", 1999,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g305-lightspeed-wireless-black-910-005282/250.jpg"],
          ["Logitech G502 X White (910-006146)", "e1b9e06a-c209-47e3-86cc-a602250cc40a", 2199,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g502-x-white-910-006146/250.jpg"],
          ["Logitech G PRO X Superlight Wireless Red (910-006784)", "1c72baa6-9d5a-4376-9b38-0a7cea058fd0", 5699,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g-pro-x-superlight-wireless-red-910-006784/250.jpg"],
          ["Logitech G305 Lightspeed Wireless Lilac (910-006022)", "bf07640a-f7e3-40f1-9c9b-f7168e7c25db", 1899,
           "https://www.3ona51.com/images/products/gaming-mouses/logitech-g305-lightspeed-wireless-lilac-910-006022/250.jpg"]]

keyboards = [["Hator Rockfall EVO TKL Optical Yellow (HTK-632)", "df473bd7-5a94-4dbb-9c19-c8025f5b221c", 2599,
              "https://www.3ona51.com/images/products/gaming-keyboards/hator-rockfall-evo-tkl-optical-yellow-htk-632/250_5.jpg"],
             ["Hator Rockfall EVO TKL Optical White (HTK-631)", "f05ef3b4-64b3-40e8-98f2-6cdef5dd44e5", 2599,
              "https://www.3ona51.com/images/products/gaming-keyboards/hator-rockfall-evo-tkl-optical-white-htk-631/250_4.jpg"],
             ["HATOR Rockfall TKL Mecha Green (HTK-620)", "801160f4-72d6-4b84-a060-052e491ac1ab", 1999,
              "https://www.3ona51.com/images/products/gaming-keyboards/hator-rockfall-tkl-mecha-green-htk-620/250.jpg"],
             ["RAZER Ornata V3 (RZ03-04460800-R3R1)", "36eebe17-5557-4219-b468-d72acfa1e06d", 2499,
              "https://www.3ona51.com/images/products/gaming-keyboards/razer-ornata-v3-rz03-04460100-r3m1/250.jpg"],
             ["HATOR Skyfall TKL PRO White (HTK-656)", "9c2e2484-1983-4ad0-8a1c-1d48dbcb8f9a", 3399,
              "https://www.3ona51.com/images/products/gaming-keyboards/hator-skyfall-tkl-pro-white-htk-656/250.jpg"],
             ["Logitech G213 Prodigy UKR (920-010740)", "02720ccb-e16b-4447-b2e7-81ba7d8e768c", 1999,
              "https://www.3ona51.com/images/products/gaming-keyboards/logitech-g213-prodigy-ukr-920-010740/250.jpg"],
             ["Logitech G715 Wireless Tactile White (920-010465)", "7b9b83e7-7cd0-450a-a09f-1409d976fde2", 5999,
              "https://www.3ona51.com/images/products/gaming-keyboards/logitech-g715-wireless-tactile-white-920-010465/250.jpg"],
             ["Logitech G713 Tactile White (920-010422)", "4a03abf7-7bdf-4258-9ef8-0b5c3380c3b1", 4999,
              "https://www.3ona51.com/images/products/gaming-keyboards/logitech-g713-tactile-white-920-010422/250.jpg"],
             ["Logitech G715 Wireless Linear White (920-010692)", "a989dba3-730d-4da2-be33-a1d7ee863768", 5999,
              "https://www.3ona51.com/images/products/gaming-keyboards/logitech-g715-wireless-linear-white-920-010692/250.jpg"],
             ["Logitech G413 TKL SE Mechanical Tactile Black (920-010447)", "0d08dd2b-cfb3-47f5-a14a-282dcbc89d69",
              2699,
              "https://www.3ona51.com/images/products/gaming-keyboards/logitech-g413-tkl-se-mechanical-tactile-black-920-010447/250.jpg"],
             ["Logitech G713 Linear White (920-010678)", "2c60f7f1-3976-4dd5-b4b7-2a5fd22d6431", 4999,
              "https://www.3ona51.com/images/products/gaming-keyboards/logitech-g713-linear-white-920-010678/250.jpg"],
             ["Logitech G413 SE Mechanical Tactile Black (920-010438)", "de277b30-bf59-4219-9929-ce79a1d8f817", 2999,
              "https://www.3ona51.com/images/products/gaming-keyboards/logitech-g413-se-mechanical-tactile-black-920-010438/250.jpg"],
             ["Razer BlackWidow V4 Pro Yellow Switch (RZ03-04681800-R3M1)", "b62cc8f3-da2d-4783-87ab-9f351f4eccc0",
              9999,
              "https://www.3ona51.com/images/products/gaming-keyboards/razer-blackwidow-v4-pro-yellow-switch-rz03-04681800-r3m1/250.jpg"],
             ["Razer BlackWidow V4 Pro Green Switch (RZ03-04680100-R3M1)", "0c8ff8d2-356b-40b9-9e0e-40735e454eb0", 9999,
              "https://www.3ona51.com/images/products/gaming-keyboards/razer-blackwidow-v4-pro-green-switch-rz03-04680100-r3m1/250.jpg"]]
