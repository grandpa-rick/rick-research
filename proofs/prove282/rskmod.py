def rsk(w):
    P=[];Q=[]
    for k,a in enumerate(w,1):
        r=0
        while True:
            if r==len(P): P.append([a]);Q.append([k]);break
            row=P[r]; j=next((j for j,b in enumerate(row) if b>a),None)
            if j is None: row.append(a);Q[r].append(k);break
            row[j],a=a,row[j]; r+=1
    return tuple(map(tuple,P)),tuple(map(tuple,Q))
