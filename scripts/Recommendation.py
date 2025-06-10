from typing import Dict, List

def Recommendations(Insights: Dict[str, Dict[str, List[str]]]) -> Dict[str, List[str]]:
  
    recs = {}
    for bank, vals in Insights.items():
        recs[bank] = []
        
        for pain in vals['painpoints']:
            recs[bank].append(f"Address customer concern: '{pain}' (e.g., improve this area)")
       
        for driver in vals['drivers']:
            recs[bank].append(f"Promote strength: '{driver}' (e.g., highlight in marketing)")
    return recs