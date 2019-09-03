# Nathan Zhu August 27, 2019 9:11 PM
# Leetcode 929 | easy | EZ
# Category: Fizzbuzz
#
# Google OA 1 hour total, 31 min 53 sec used, rating beating 85% of all users


def numUniqueEmails(self, emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    # Rules ".", all dots are ignored.
    
    # Rules, "+", everything after "+" is ignored.
    
    # None of these rules apply to the domain name.
    
    # Algo,
    # 1. We split based off of @ sign into local and domain.
    # 2. We go thru all the [local, domain] pairs.  
    #
    # 3. Return size of all unique pairs.
    
    
    emails_list = [email.split("@") for email in emails]
    processed = list()
    for local, domain in emails_list:
        if "+" in local: local = local.split("+")[0]
        local = local.replace(".", "")
        processed.append((local, domain))
        
    return len(set(processed))