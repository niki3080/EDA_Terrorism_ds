def translate_attack_types(df, column="attack_type"):
    
    attack_type_ru = {
        "Armed Assault": "Вооруженное нападение",
        "Assassination": "Покушение",
        "Bombing/Explosion": "Взрыв",
        "Facility/Infrastructure Attack": "Атака на инфраструктуру",
        "Hostage Taking (Kidnapping)": "Захват заложников",
        "Hostage Taking (Barricade Incident)": "Захват заложников",
        "Hijacking": "Угон транспорта",
        "Unarmed Assault": "Нападение без оружия",
        "Unknown": "Unknown"
    }

    df = df.copy()
    df[column] = df[column].replace(attack_type_ru)

    return df



