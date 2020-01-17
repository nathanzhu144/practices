# Nathan Zhu Jan 11th, 2020, 8:09 pm
# Leetcode 721 | medium | kinda hard 
# Category: union find
# So, I knew it was UF, but couldn't formulate it well.


def accountsMerge(accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """
    
    parent, email_to_name = dict(), dict()
    
    def union(a, b):
        parent[find(a)] = find(b)
        
    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]
    
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in parent:
                parent[email] = email
            email_to_name[email] = name
            
            union(email, account[1])
            
    graph = collections.defaultdict(list)
    for email in parent:
        graph[find(email)].append(email)
        
    return [[email_to_name[root]] + sorted(emails) for root, emails in graph.items()]