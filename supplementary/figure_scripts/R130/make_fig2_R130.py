import sys
from style_R119 import *
from matplotlib.patches import Polygon
variant=sys.argv[1]
TITLES=['Task path','IK solutions','Selection','Joint curve','Timing law']
MAIN=[r'$x(s),\ s\in[0,1]$','at each pose','along the path',r'$q(s)$',r'$s(t)\ \rightarrow\ \dot q,\ \ddot q$']
SUB=[r'tolerance set $X_{task}(s)$','several branches','branch, mode and\nsingular events','geometric lift, Eq. (1)','Eq. (2); torque needs\na dynamic model']
# (header, [refs]) groups per stage
GROUPS={1:[('Branch labels',['Gong et al., 2019']),('Global pseudoinverse',['Hauser & Emmons, 2018'])],
 2:[('Directed-graph search',['Rakita et al., 2019','Elias & Wen, 2025a']),('Reconfiguration edges',['Wang et al., 2024']),
    ('Cuspidal: nonsingular',['Wenger & Chablat, 2023','Salunkhe et al., 2025']),('UR-like: via singularity',['Boschi et al., 2026'])],
 4:[('Joint and dynamic\nlimits',['Ferrentino et al., 2024','Yin et al., 2024, 2025','Y. Zhang & Kikuuwe, 2026'])]}
CHIP={1:BLUE,2:GREEN,4:PEACH}
IND='Industrial toolpath planning: tolerances, collision constraints, controller interpolation (Weingartshofer et al., 2023)'
FS=7.0; FSB=7.4
WT=[0.92,1.0,1.1,0.92,1.14]
def cols(x0,total,gap):
    avail=total-4*gap; u=avail/sum(WT); xs=[];x=x0
    for w in WT: xs.append((x,w*u)); x+=w*u+gap
    return xs

GAPG=3.0
def hh(h,gh): return gh*(h.count('\n')+1)
def groups_height(i,gh,ch):
    return sum(hh(h,gh)+len(r)*ch+GAPG for h,r in GROUPS.get(i,[]))-GAPG
if variant=='A':
    W=450.0; M=3.0; gap=6.0; CX=cols(M,W-2*M,gap)
    chev_h=32; tip=9
    gh,ch=11.5,12.5
    top_h=40
    cards_h=[top_h+(groups_height(i,gh,ch)+10 if i in GROUPS else 0) for i in range(5)]
    bar_h=22
    H=M+chev_h+5+max(cards_h)+10+bar_h+M
    fig,ax=canvas(6.26,6.26*H/W,W,H)
    ytop=H-M-chev_h
    for i in range(5):
        x,cw=CX[i]
        pts=[(x,ytop),(x+cw-tip,ytop),(x+cw,ytop+chev_h/2),(x+cw-tip,ytop+chev_h),(x,ytop+chev_h)]
        if i>0: pts=[(x,ytop),(x+cw-tip,ytop),(x+cw,ytop+chev_h/2),(x+cw-tip,ytop+chev_h),(x,ytop+chev_h),(x+tip,ytop+chev_h/2)]
        ax.add_patch(Polygon(pts,closed=True,fc=BLUE2 if False else BLUE,ec=BLACK,lw=0.9,zorder=2,joinstyle='round'))
        ax.text(x+cw/2+(tip/2 if i>0 else -1),ytop+chev_h/2,TITLES[i],ha='center',va='center',fontsize=8.0,fontweight='bold',color=BLACK,zorder=3)
        ch_top=ytop-5; h=cards_h[i]
        box(ax,x,ch_top-h,cw,h,fc=WHITE,r=2.0,lw=0.9)
        ax.text(x+cw/2,ch_top-11,MAIN[i],ha='center',va='center',fontsize=FSB,color=BLACK)
        ax.text(x+cw/2,ch_top-26,SUB[i],ha='center',va='center',fontsize=6.3,color='#222222',linespacing=1.1)
        if i in GROUPS:
            ax.plot([x+4,x+cw-4],[ch_top-top_h+1,ch_top-top_h+1],color=GREY,lw=0.5,ls=(0,(2,2)))
            y=ch_top-top_h-5
            for hdr,refs in GROUPS[i]:
                n=hdr.count('\n')+1
                ax.text(x+5,y-hh(hdr,gh)/2+2.5,hdr,ha='left',va='center',fontsize=FS-0.4,fontweight='bold',color=BLACK,linespacing=1.05); y-=hh(hdr,gh)
                for r in refs:
                    box(ax,x+4,y-ch+2.2,cw-8,ch-3.0,fc=CHIP[i],ec='none',lw=0,r=2.0,z=2)
                    ax.text(x+cw/2,y-ch/2+1.1,r,ha='center',va='center',fontsize=FS-0.5,color=BLACK,zorder=3); y-=ch
                y-=GAPG
    by=M
    box(ax,M,by,W-2*M,bar_h,fc=LIGHT,r=2.5,lw=0.9)
    ax.text(W/2,by+bar_h/2,IND,ha='center',va='center',fontsize=6.9,color=BLACK)
    name='figure2_pipeline_R130_A'
else:
    W=450.0; M=3.0; lab=50.0; gap=0.0; CX=cols(M+lab,W-2*M-lab,0.0)
    gh,ch=10.5,11.2
    hdr_h=22; form_h=34; refs_h=groups_height(2,gh,ch)+10; ind_h=22
    H=M+hdr_h+form_h+refs_h+ind_h+M
    fig,ax=canvas(6.26,6.26*H/W,W,H)
    x0=M+lab
    rows=[('Stage',hdr_h),('Object',form_h),('Studies',refs_h),('Industrial',ind_h)]
    y=H-M; ys={}
    for nm,h in rows: ys[nm]=(y-h,h); y-=h
    # outer frame
    box(ax,M,M,W-2*M,H-2*M,fc=WHITE,r=3.0,lw=1.0,z=0)
    # row labels
    for nm,(yb,h) in ys.items():
        ax.text(M+lab/2,yb+h/2,nm,ha='center',va='center',fontsize=7.4,fontweight='bold',color=BLACK,rotation=0)
    # header cells
    yb,h=ys['Stage']
    for i in range(5):
        x,cw=CX[i]
        box(ax,x+1.5,yb+2,cw-3,h-4,fc=BLUE,r=2.5,lw=0.9,z=2)
        ax.text(x+cw/2,yb+h/2,TITLES[i],ha='center',va='center',fontsize=7.8,fontweight='bold',zorder=3)
        if i<4: arrow(ax,x+cw-1.0,yb+h/2,x+cw+1.0,yb+h/2,lw=0.9)
    yb,h=ys['Object']
    for i in range(5):
        x,cw=CX[i]
        ax.text(x+cw/2,yb+h-10,MAIN[i],ha='center',va='center',fontsize=7.2)
        ax.text(x+cw/2,yb+11,SUB[i],ha='center',va='center',fontsize=6.2,color='#222222',linespacing=1.1)
    yb,h=ys['Studies']
    for i in GROUPS:
        x,cw=CX[i]; yy=yb+h-6
        for hdr,refs in GROUPS[i]:
            ax.text(x+4,yy-hh(hdr,gh)/2+2,hdr,ha='left',va='center',fontsize=6.6,fontweight='bold',linespacing=1.05); yy-=hh(hdr,gh)
            for r in refs:
                box(ax,x+3,yy-ch+2.0,cw-6,ch-2.8,fc=CHIP[i],ec='none',lw=0,r=2.0,z=2)
                ax.text(x+cw/2,yy-ch/2+1.0,r,ha='center',va='center',fontsize=6.4,zorder=3); yy-=ch
            yy-=GAPG
    yb,h=ys['Industrial']
    box(ax,x0+1.5,yb+2.5,W-M-x0-3,h-5,fc=LIGHT,r=2.5,lw=0.9,z=2)
    ax.text((x0+W-M)/2,yb+h/2,IND,ha='center',va='center',fontsize=6.6,zorder=3)
    # row separators and column guides
    for nm in ['Stage','Object','Studies']:
        yb,h=ys[nm]; ax.plot([M+3,W-M-3],[yb,yb],color=GREY,lw=0.6)
    for i in range(1,5):
        x=CX[i][0]; ax.plot([x,x],[ys['Studies'][0]+2,ys['Object'][0]+ys['Object'][1]-2],color='#cfd3d9',lw=0.5,ls=(0,(2,2)))
    ax.plot([x0,x0],[M+3,H-M-3],color=GREY,lw=0.6)
    name='figure2_pipeline_R130_B'
save(fig,name)
print(name,H)
