from Propositional_KB_agent import KB, Rule, KBase, theorem1, theorem2, theorem3, theorem4, theorem5

def forwardchain(KB, theorem):
    print("\nstart forward chain:", theorem)
    new_fact = True
    while new_fact:
        new_fact = False
        for rule in KB.RB:
            if not KB.is_in_FB(rule.then_part):
                antecedents = all(KB.is_in_FB(cond) for cond in rule.cond_part)
                if antecedents:
                    KB.add_fact(rule.then_part)
                    new_fact = True
                    print("\nrule attempted: ", rule.name)
                    print("\nif ", rule.cond_part, " then ", rule.then_part)
                    print("\nattempt successful, adding rule: ", rule.then_part)                    
                    if rule.then_part == theorem:
                        print("\nthis proves theorem:", theorem)
                        return True
        if not new_fact:
            break
    if KB.is_in_FB(theorem):
        print("\nthis proves theorem:", theorem)
        return True
    print("\nfailure in proving theorem:", theorem)
    return False
theorems = [theorem1, theorem2, theorem3, theorem4, theorem5]

for i, thrm in enumerate(theorems, start=1):
    print("\n ////// theorem: ", thrm,  "//////")
    KBase.reset_FB(['gives_milk','chews_cud','has_long_legs','has_a_long_neck','has_a_tawny_color','has_dark_spots'])
    result = forwardchain(KBase, thrm)
    print("\nfact base now:")
    KBase.print_FB()
