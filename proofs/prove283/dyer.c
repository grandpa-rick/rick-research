/* KL polynomials P_{u,top} for all u in a Bruhat interval, via Dyer's formula
   Rtilde_{u,y} = sum over reflection-order-increasing Bruhat-graph paths u->y of t^{#edges}.
   Input (stdin): N E top ; then N lengths (vertices sorted by length ascending) ; then E lines "a b label" (a->b, l(b)>l(a)),
   edges sorted by b then label. Output: for each u: index, coeffs of P_{u,top}. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define K 16
typedef long long ll;
int N,E,top,*len,*ea,*eb,*el,*inStart; ll (*f)[K]; ll (*P)[K];
int main(){
  if(scanf("%d %d %d",&N,&E,&top)!=3) return 1;
  len=malloc(N*sizeof(int)); for(int i=0;i<N;i++) scanf("%d",&len[i]);
  ea=malloc(E*sizeof(int)); eb=malloc(E*sizeof(int)); el=malloc(E*sizeof(int));
  for(int e=0;e<E;e++) scanf("%d %d %d",&ea[e],&eb[e],&el[e]);
  inStart=calloc(N+1,sizeof(int)); for(int e=0;e<E;e++) inStart[eb[e]+1]++; for(int i=0;i<N;i++) inStart[i+1]+=inStart[i];
  /* out-edges grouped by source a: build list */
  int *outStart=calloc(N+1,sizeof(int)),*outE=malloc(E*sizeof(int)),*fill=calloc(N,sizeof(int));
  for(int e=0;e<E;e++) outStart[ea[e]+1]++; for(int i=0;i<N;i++) outStart[i+1]+=outStart[i];
  for(int e=0;e<E;e++){int a=ea[e]; outE[outStart[a]+fill[a]++]=e;}
  f=calloc(E,sizeof(*f)); P=calloc(N,sizeof(*P));
  int L=len[top]; ll R[K]; ll F[K]; ll binom[K][K]; memset(binom,0,sizeof binom);
  for(int i=0;i<K;i++){binom[i][0]=1; for(int j=1;j<=i;j++) binom[i][j]=binom[i-1][j-1]+binom[i-1][j];}
  ll pre[K]; int *vst=malloc(N*sizeof(int)),*est=malloc(E*sizeof(int)); for(int i=0;i<N;i++) vst[i]=-1; for(int e=0;e<E;e++) est[e]=-1;
  for(int u=N-1;u>=0;u--){
    if(u==top){P[u][0]=1; continue;}
    for(int a=u;a<N;a++){
      if(a!=u && vst[a]!=u) continue;
      int s=inStart[a],t=inStart[a+1];
      for(int oi=outStart[a];oi<outStart[a+1];oi++){
        int e=outE[oi], lab=el[e];
        memset(pre,0,sizeof pre);
        if(a==u) pre[0]=1;
        else for(int e2=s;e2<t && el[e2]<lab;e2++) if(est[e2]==u) for(int k=0;k<K-1;k++) pre[k]+=f[e2][k];
        int nz=0; for(int k=0;k<K-1;k++){ f[e][k+1]=pre[k]; if(pre[k]) nz=1;} f[e][0]=0;
        if(nz){ est[e]=u; vst[eb[e]]=u; }
      }
    }
    /* F = sum_{y>u} R_{u,y} P_{y,top}; R_{u,y}(q)=sum_k c_k q^{(l-k)/2}(q-1)^k */
    memset(F,0,sizeof F); int lu=len[u];
    for(int y=u+1;y<N;y++){
      if(vst[y]!=u) continue;
      memset(R,0,sizeof R); int nz=0; int l=len[y]-lu;
      for(int e=inStart[y];e<inStart[y+1];e++) if(est[e]==u) for(int k=0;k<K;k++) if(f[e][k]){
        ll c=f[e][k]; nz=1; int sh=(l-k)/2;
        for(int j=0;j<=k;j++){ ll term=binom[k][j]*(((k-j)&1)?-1:1); R[sh+j]+=c*term; } }
      if(!nz) continue;
      int has=0; for(int k=0;k<K;k++) if(P[y][k]) has=1; if(!has) continue;
      for(int i=0;i<K;i++) if(R[i]) for(int j=0;i+j<K;j++) F[i+j]+=R[i]*P[y][j];
    }
    int l=L-lu;
    /* P_{u,top} = -(F truncated to degree < l/2) ; if u not <= top, F should be 0 */
    for(int i=0;2*i<l;i++) P[u][i]=-F[i];
  }
  for(int u=0;u<N;u++){printf("%d",u); for(int k=0;k<(L+2)/2&&k<K;k++) printf(" %lld",P[u][k]); printf("\n");}
  return 0;
}
