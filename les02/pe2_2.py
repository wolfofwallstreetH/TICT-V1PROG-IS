cijferICOR = 10
cijferPROG = 10
cijferCSN = 10

totaalCijfersBlok1 = (cijferICOR + cijferPROG + cijferCSN)

gemiddelde = (totaalCijfersBlok1 / 3)
beloning = totaalCijfersBlok1 * 30
overzicht = ('mijn cijfers ' + str(gemiddelde) + ' leveren een beloning van ' + str(beloning) )
print(overzicht)