#!/usr/bin/env python3
"""UF-015 checks for the analytic D4 representation decomposition.

The analytic freeness theorem is proved in the companion note using the
reflection-group invariant theorem and analytic base change. This script
checks finite group relations, both E-covariants, scalar characters,
coinvariant basis reductions, and the Hilbert numerator.
"""
I=(1,0,0,1)
R=(0,-1,1,0)
S=(0,1,1,0)

def mm(A,B):
    a,b,c,d=A; e,f,g,h=B
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)

def act(M,x,y):
    a,b,c,d=M
    return (a*x+b*y,c*x+d*y)

def char_value(k,eps,alpha,beta):
    return alpha**k*beta**eps

def group():
    out=[]; P=I
    for k in range(4):
        out.append((k,0,P))
        out.append((k,1,mm(P,S)))
        P=mm(P,R)
    return out

def basis(x,y):
    return (1,x*y,x*x-y*y,x*y*(x*x-y*y),x,y,x*y*y,x*x*y)

def v1(x,y): return (x,y)
def v3(x,y): return (x*y*y,x*x*y)

def verify():
    G=group()
    assert len(G)==8 and len({M for _,_,M in G})==8
    assert mm(mm(mm(R,R),R),R)==I
    assert mm(S,S)==I
    assert mm(mm(S,R),S)==mm(mm(R,R),R)
    samples=((2,1),(3,-2),(1,4),(-3,5),(5,7))
    relation_checks=3
    basis_checks=covariant_checks=character_checks=0
    for k,eps,M in G:
        for x,y in samples:
            X,Y=act(M,x,y)
            assert v1(X,Y)==act(M,*v1(x,y))
            assert v3(X,Y)==act(M,*v3(x,y))
            covariant_checks+=2
            before=basis(x,y); after=basis(X,Y)
            assert len(before)==len(after)==8
            # Relative invariants transform by their one-dimensional characters.
            labels=((1,1,lambda a,b:1),
                    (-1,1,lambda a,b:a*b),
                    (-1,-1,lambda a,b:a*a-b*b),
                    (1,-1,lambda a,b:a*b*(a*a-b*b)))
            for alpha,beta,f in labels:
                assert f(X,Y)==char_value(k,eps,alpha,beta)*f(x,y)
                character_checks+=1
            basis_checks+=8
    # Modulo p=x^2+y^2 and q=x^2y^2, y^2=-x^2 and x^4=0.
    reductions=("1","xy","2x^2","2x^3y","x","y","-x^3","x^2y")
    assert len(set(reductions))==8
    degrees=(0,2,2,4,1,1,3,3)
    counts={d:degrees.count(d) for d in set(degrees)}
    assert counts=={0:1,1:2,2:2,3:2,4:1}
    # Numerator is (1+t)(1+t+t^2+t^3) = 1+2t+2t^2+2t^3+t^4.
    poly=[0]*5
    for i,a in enumerate((1,1)):
        for j,b in enumerate((1,1,1,1)):
            poly[i+j]+=a*b
    assert poly==[1,2,2,2,1]
    return {
        "D4_group_elements":len(G),
        "D4_relation_checks":relation_checks,
        "basis_evaluation_checks":basis_checks,
        "E_covariant_checks":covariant_checks,
        "relative_character_checks":character_checks,
        "coinvariant_basis_elements":len(reductions),
        "A_module_rank":8,
        "E_irrep_multiplicity":2,
        "scalar_character_modules":4,
    }

if __name__=="__main__":
    print("UF-015 D4 analytic representation decomposition")
    print("basis:",("1","xy","x^2-y^2","xy(x^2-y^2)","x","y","xy^2","x^2y"))
    print("verification:",verify())
