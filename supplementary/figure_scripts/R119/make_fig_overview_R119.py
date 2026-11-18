from style_R119 import *
W,H=100,39.8
fig,ax=canvas(6.26,6.26*H/W,W,H)
m=1.0; full=W-2*m
# scope bar
sh=5.2; sy=H-sh-0.6
box(ax,m,sy,full,sh,fc=BLUE,r=1.2)
ax.text(W/2,sy+sh/2,'Scope: fixed-base serial manipulators on prescribed Cartesian paths; core case: 6-DOF industrial arm',ha='center',va='center',fontsize=6.4,color=BLACK)
# three dimension boxes
gap=2.2; bw=(full-2*gap)/3; bh=16.4; by=sy-2.4-bh
heads=['Path continuation\nand events','Constraint enforcement\nand domain','Trajectory\nverification']
qs=['Which connected object is selected;\nhow are branch and singularity\nevents handled?',
    'Which hard constraints and soft\nobjectives are imposed, and\nwhere are they checked?',
    'Is the same reconstructed motion\nchecked for the claim made?']
refs=['§2.2, §3.2','§2.3','§3.1, §3.3']
for i in range(3):
    x=m+i*(bw+gap)
    box(ax,x,by,bw,bh,fc=BLUE,r=1.3)
    ax.add_patch(Circle((x+3.6,by+bh-4.1),2.0,fc=BLACK,ec=BLACK,zorder=3))
    ax.text(x+3.6,by+bh-4.15,str(i+1),color='white',ha='center',va='center',fontsize=7,fontweight='bold',zorder=4)
    ax.text(x+6.9,by+bh-4.1,heads[i],ha='left',va='center',fontsize=6.9,fontweight='bold',color=BLACK,linespacing=1.05)
    ax.text(x+2.2,by+bh-9.8 if i<2 else by+bh-8.0,qs[i],ha='left',va='center',fontsize=5.9,color=BLACK,linespacing=1.15)
    ax.text(x+bw-2.0,by+1.6,refs[i],ha='right',va='center',fontsize=6.0,fontweight='bold',color=BLACK)
# chips in box 3
x3=m+2*(bw+gap)
cx=x3+2.2
for lab in ['samples','edges','curve','timed']:
    w=len(lab)*0.66+2.3
    box(ax,cx,by+3.0,w,2.6,fc=GREEN,r=0.7,lw=0.7)
    ax.text(cx+w/2,by+4.3,lab,ha='center',va='center',fontsize=5.0,color=BLACK)
    cx+=w+0.9
# arrow
ay0=by-0.1; ay1=by-2.3
arrow(ax,W/2,ay0,W/2,ay1+0.0,lw=1.0)
# applied container
ch=11.6; cy=ay1-ch-0.2
box(ax,m,cy,full,ch,fc=LIGHT,r=1.2,lw=0.9)
inner=(full-4*1.4)/3
apps=[('Applied in §4.1–4.2','Cross-study comparison and\n78-study evidence matrix'),
      ('Applied in §4.3','Three findings on continuation,\nconstraints and verification'),
      ('Applied in §5','Four-level verification\nbenchmark on the UR5e')]
for i,(t,d) in enumerate(apps):
    x=m+1.4+i*(inner+1.4)
    box(ax,x,cy+1.3,inner,ch-2.6,fc=WHITE,r=0.9,lw=0.8)
    ax.text(x+2.0,cy+ch-4.0,t,ha='left',va='center',fontsize=6.3,fontweight='bold',color=BLACK)
    ax.text(x+2.0,cy+3.6,d,ha='left',va='center',fontsize=5.6,color=BLACK,linespacing=1.15)
print('bottom',cy)
save(fig,'figure3_overview_R119')
