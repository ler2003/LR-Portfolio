from Propositional_KB_agent import KB, Rule, KBase, theorem1, theorem2, theorem3, theorem4, theorem5

def backwardchain(KB, theorem):
    print("start backward chain: ", theorem)
    if KB.is_in_FB(theorem):
        print("theorem ", theorem, " already exists in fact base")
        return True
    rule_applies = [rule for rule in KB.RB if rule.then_part == theorem]
    if not rule_applies:
        print("failure in proving theorem: ", theorem)
        return False
    for rule in rule_applies:
        print("rule attemted: ", rule.name)
        print("if ", rule.cond_part, " then ", rule.then_part)
        all_rules_done = True
        for antecedent in rule.cond_part:
            if not KB.is_in_FB(antecedent):
                print("antedecent to prove: ", antecedent)
                if not backwardchain(KB, antecedent):
                    all_rules_done = False
                    print("failure to prove antecedent: ", antecedent)
                    break
        if all_rules_done:
            KB.add_fact(theorem)
            print("attempt successful, adding theorem: ", theorem)
            return True
        else:
            print("rule ", rule.name, "failed to prove theorem: ", theorem)
    print("\nfailure in proving theorem:", theorem)
    return False
theorems = [theorem1, theorem2, theorem3, theorem4, theorem5]

for i, thrm in enumerate(theorems, start=1):
    print("\n ////// theorem: ", thrm,  "//////")
    KBase.reset_FB(['gives_milk','chews_cud','has_long_legs','has_a_long_neck','has_a_tawny_color','has_dark_spots'])
    result = backwardchain(KBase, thrm)
    print("\nfact base now:")
    KBase.print_FB()
