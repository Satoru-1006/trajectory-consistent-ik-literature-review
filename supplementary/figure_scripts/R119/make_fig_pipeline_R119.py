from style_R119 import *
W,H=100,42.0
fig,ax=canvas(6.26,6.26*H/W,W,H)
bw,bh,gap=16.8,13.0,3.2
x0=(W-5*bw-4*gap)/2; ytop=H-bh-0.8
titles=['Task path','IK solutions','Selection','Joint curve','Timing law']
mids=[r'$x(s),\ s\in[0,1]$','at each pose','along the path',r'$q(s)$',r'$s(t)\ \rightarrow\ \dot q,\ \ddot q$']
subs=[r'tolerance set $X_{task}(s)$','several branches','branch, mode and\nsingular events','geometric lift, Eq. (1)','Eq. (2); torque needs\na dynamic model']
cx=[]
for i in range(5):
    x=x0+i*(bw+gap); cx.append(x+bw/2)
    box(ax,x,ytop,bw,bh,fc=BLUE,r=1.3)
    ax.text(x+bw/2,ytop+bh-3.0,titles[i],ha='center',va='center',fontsize=7.4,fontweight='bold',color=BLACK)
    ax.text(x+bw/2,ytop+bh-6.9,mids[i],ha='center',va='center',fontsize=7.4,color=BLACK)
    ax.text(x+bw/2,ytop+2.7,subs[i],ha='center',va='center',fontsize=5.6,color='#222222',linespacing=1.05)
    if i<4: arrow(ax,x+bw+0.5,ytop+bh/2,x+bw+gap-0.5,ytop+bh/2,lw=1.1)
# detail boxes
dh=14.2; dy=ytop-3.0-dh
def detail(xc,w,cols,left=None,link=None):
    x=xc-w/2 if left is None else left; box(ax,x,dy,w,dh,fc=WHITE,r=1.0,lw=0.8)
    n=len(cols); cw=w/n
    for k,col in enumerate(cols):
        for j,(txt,bold) in enumerate(col):
            ax.text(x+k*cw+1.5,dy+dh-2.1-j*2.55,txt,ha='left',va='center',fontsize=5.5,fontweight='bold' if bold else 'normal',color=BLACK)
    ax.plot([xc if link is None else link]*2,[ytop-0.1,dy+dh+0.1],color=GREY,lw=0.7,ls=(0,(1,2)),zorder=0)
detail(cx[1],bw+1.0,[[('Branch labels',1),('Gong et al., 2019',0),('Global pseudoinverse',1),('Hauser & Emmons, 2018',0)]])
detail(cx[2],36.0,left=cx[1]+(bw+1.0)/2+1.2,link=cx[2],cols=[[('Directed-graph search',1),('Rakita et al., 2019',0),('Elias & Wen, 2025a',0),('Reconfiguration edges',1),('Wang et al., 2024',0)],
                   [('Cuspidal: nonsingular',1),('Wenger & Chablat, 2023',0),('Salunkhe et al., 2025',0),('UR-like: via singularity',1),('Boschi et al., 2026',0)]])
detail(cx[4],bw+1.0,[[('Joint and dynamic limits',1),('Ferrentino et al., 2024',0),('Yin et al., 2024, 2025',0),('Y. Zhang & Kikuuwe, 2026',0)]])
# bottom bar
bh2=5.6; by=dy-2.8-bh2
box(ax,x0,by,5*bw+4*gap,bh2,fc=LIGHT,r=1.0,lw=0.8)
ax.text(W/2,by+bh2/2,'Industrial toolpath planning: tolerances, collision constraints, controller interpolation (Weingartshofer et al., 2023)',ha='center',va='center',fontsize=5.9,color=BLACK)
print('min y',by)
save(fig,'figure2_pipeline_R119')
