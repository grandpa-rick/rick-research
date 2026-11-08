/* dyer2: P_{x,z} in S_n via Dyer's path formula on [x,z] (lex reflection order on position pairs,
   same convention as dyer.c), with the double-coset shortcut:
   P_{y,z} = P_{rep(y),z}, where rep(y) = max of W_K y W_J, K = L(z), J = R(z)
   (valid because P_{y,z} = P_{sy,z} for s in L(z) and P_{y,z} = P_{ys,z} for s in R(z)).
   So the inversion formula q^{l(z)-l(u)} P_{u,z}(1/q) - P_{u,z} = sum_{u<y<=z} R_{u,y} P_{rep(y),z}
   only has to be solved for double-max u, top-down.
   R~_{u,y}(t) is computed by DP over edges, using prefix sums over label-sorted in-edges.
   Input: n, x[n], z[n] (1-based values). Optional argv[1]="all": treat every u as a target (no coset shortcut; for validation).
   Output: P_{x,z} coefficients; with "dump" the P of every target u. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
typedef long long ll; typedef uint64_t u64;
#define K 24
int n;
static inline int get(u64 w,int i){return (w>>(4*i))&15;}
static inline u64 setv(u64 w,int i,int v){return (w&~((u64)15<<(4*i)))|((u64)v<<(4*i));}
static inline u64 swp(u64 w,int i,int j){int a=get(w,i),b=get(w,j);return setv(setv(w,i,b),j,a);}
int len_of(u64 w){int c=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(get(w,i)>get(w,j))c++;return c;}
/* hash */
u64 *hk; int *hv; u64 hmask;
static inline u64 hh(u64 k){k^=k>>33;k*=0xff51afd7ed558ccdULL;k^=k>>33;k*=0xc4ceb9fe1a85ec53ULL;k^=k>>33;return k;}
int hget(u64 k){u64 p=hh(k)&hmask;while(hv[p]>=0){if(hk[p]==k)return hv[p];p=(p+1)&hmask;}return -1;}
void hput(u64 k,int v){u64 p=hh(k)&hmask;while(hv[p]>=0){if(hk[p]==k){hv[p]=v;return;}p=(p+1)&hmask;}hk[p]=k;hv[p]=v;}
int Xr[16][16]; /* sorted prefixes of x */
int geqx(u64 y){int b[16];for(int k=1;k<n;k++){int m=0;for(int i=0;i<k;i++){int v=get(y,i),p=m++;while(p>0&&b[p-1]>v){b[p]=b[p-1];p--;}b[p]=v;}for(int i=0;i<k;i++)if(Xr[k][i]>b[i])return 0;}return 1;}
int Rz[16],Lz[16];
u64 rep(u64 y){ /* raise to max of W_K y W_J */
  int ch=1; while(ch){ch=0;
    for(int i=0;i+1<n;i++) if(Rz[i]&&get(y,i)<get(y,i+1)){y=swp(y,i,i+1);ch=1;}
    for(int v=0;v+1<n;v++) if(Lz[v]){int pi=-1,pj=-1;for(int i=0;i<n;i++){if(get(y,i)==v)pi=i;if(get(y,i)==v+1)pj=i;}
      if(pi<pj){y=swp(y,pi,pj);ch=1;}}
  } return y;}
int main(int argc,char**argv){
  int all=argc>1&&!strcmp(argv[1],"all"); int dump=argc>2&&!strcmp(argv[2],"dump");
  if(scanf("%d",&n)!=1)return 1; u64 x=0,z=0; int t;
  for(int i=0;i<n;i++){scanf("%d",&t);x=setv(x,i,t-1);} for(int i=0;i<n;i++){scanf("%d",&t);z=setv(z,i,t-1);}
  for(int k=1;k<n;k++){int b[16];for(int i=0;i<k;i++)b[i]=get(x,i);for(int i=0;i<k;i++)for(int j=i+1;j<k;j++)if(b[j]<b[i]){int c=b[i];b[i]=b[j];b[j]=c;}for(int i=0;i<k;i++)Xr[k][i]=b[i];}
  for(int i=0;i+1<n;i++){Rz[i]=get(z,i)>get(z,i+1);}
  for(int v=0;v+1<n;v++){int pi=0,pj=0;for(int i=0;i<n;i++){if(get(z,i)==v)pi=i;if(get(z,i)==v+1)pj=i;}Lz[v]=pj<pi;}
  if(all){memset(Rz,0,sizeof Rz);memset(Lz,0,sizeof Lz);}
  clock_t T0=clock();
  /* BFS down by covers */
  int cap=1<<25; u64 *V=malloc(sizeof(u64)*cap); int N=0; hmask=(1ULL<<26)-1; hk=malloc(sizeof(u64)*(hmask+1)); hv=malloc(sizeof(int)*(hmask+1)); memset(hv,-1,sizeof(int)*(hmask+1));
  int lz=len_of(z),lx=len_of(x); V[N]=z; hput(z,N++); int lo=0;
  int *lvstart=calloc(64,sizeof(int)); int nl=0; lvstart[0]=0;
  while(lo<N){int hi=N; lvstart[++nl]=hi;
    for(int a=lo;a<hi;a++){u64 w=V[a];
      for(int i=0;i<n;i++){int wi=get(w,i),m=-1;for(int j=i+1;j<n;j++){int wj=get(w,j);if(wj<wi&&wj>m){u64 v=swp(w,i,j);m=wj;if(hget(v)<0&&geqx(v)){if(N>=cap){fprintf(stderr,"cap\n");return 2;}V[N]=v;hput(v,N++);}}}}}
    lo=hi;}
  fprintf(stderr,"interval size %d lx %d lz %d time %.1fs\n",N,lx,lz,(double)(clock()-T0)/CLOCKS_PER_SEC);
  /* reindex ascending length: reverse BFS order (BFS order is descending length) */
  u64 *A=malloc(sizeof(u64)*N); int *Ln=malloc(sizeof(int)*N);
  for(int i=0;i<N;i++){A[i]=V[N-1-i];} free(V);
  memset(hv,-1,sizeof(int)*(hmask+1)); for(int i=0;i<N;i++){hput(A[i],i);Ln[i]=len_of(A[i]);}
  /* edges a->b (b = a*(i j), a[i]<a[j]), label = lex index of (i,j). in-CSR by b sorted by label */
  int lab[16][16];{int c=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)lab[i][j]=c++;}
  ll E=0; int *indeg=calloc(N+1,sizeof(int)), *outdeg=calloc(N+1,sizeof(int));
  for(int a=0;a<N;a++){u64 w=A[a];for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(get(w,i)<get(w,j)){int b=hget(swp(w,i,j));if(b>=0){indeg[b]++;outdeg[a]++;E++;}}}
  fprintf(stderr,"edges %lld\n",E);
  ll *inS=malloc(sizeof(ll)*(N+1)),*outS=malloc(sizeof(ll)*(N+1)); inS[0]=outS[0]=0;
  for(int i=0;i<N;i++){inS[i+1]=inS[i]+indeg[i];outS[i+1]=outS[i]+outdeg[i];}
  /* in-edges of b listed in label order: iterate (i,j) lex for b, source a=b*(i j) with a[i]<a[j] i.e. b[i]>b[j] */
  int *inSrc=malloc(sizeof(int)*E); unsigned short *inLab=malloc(2*E);
  for(int b=0;b<N;b++){ll p=inS[b];u64 w=A[b];for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(get(w,i)>get(w,j)){int a=hget(swp(w,i,j));if(a>=0){inSrc[p]=a;inLab[p]=lab[i][j];p++;}}}
  /* out-edges of a: target b, slot in b's in-list, pos = #in-edges of a with label < this label */
  ll *outSlot=malloc(sizeof(ll)*E); int *outPos=malloc(sizeof(int)*E); int *outDst=malloc(sizeof(int)*E);
  for(int a=0;a<N;a++){ll p=outS[a];u64 w=A[a];for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(get(w,i)<get(w,j)){int b=hget(swp(w,i,j));if(b<0)continue;int L=lab[i][j];
      ll s;for(s=inS[b];s<inS[b+1];s++)if(inSrc[s]==a)break; outSlot[p]=s; outDst[p]=b;
      int c=0;for(ll q=inS[a];q<inS[a+1];q++)if(inLab[q]<L)c++; outPos[p]=c; p++;}}
  fprintf(stderr,"graph built %.1fs\n",(double)(clock()-T0)/CLOCKS_PER_SEC);
  /* targets */
  int *isT=calloc(N,sizeof(int)); int *repI=malloc(sizeof(int)*N); int nT=0;
  for(int i=0;i<N;i++){u64 r=rep(A[i]); int ri=hget(r); if(ri<0){fprintf(stderr,"rep outside interval!\n");return 3;} repI[i]=ri; if(ri==i){isT[i]=1;nT++;}}
  int xi=hget(x),zi=hget(z); fprintf(stderr,"targets %d x is target %d\n",nT,isT[xi]);
  ll (*G)[K]=malloc(sizeof(ll)*K*E); if(!G){fprintf(stderr,"oom\n");return 4;}
  int *est=malloc(sizeof(int)*E); for(ll e=0;e<E;e++)est[e]=-1;
  int *vst=malloc(sizeof(int)*N); for(int i=0;i<N;i++)vst[i]=-1;
  ll (*P)[K]=calloc(N,sizeof(ll)*K);
  int maxL=lz+1; int **bk=malloc(sizeof(int*)*(maxL+1)); int *bn=calloc(maxL+1,sizeof(int)),*bc=calloc(maxL+1,sizeof(int));
  for(int l=0;l<=maxL;l++){bc[l]=0;} for(int i=0;i<N;i++)bc[Ln[i]]++; for(int l=0;l<=maxL;l++)bk[l]=malloc(sizeof(int)*(bc[l]+1));
  ll binom[K][K];memset(binom,0,sizeof binom);for(int i=0;i<K;i++){binom[i][0]=1;for(int j=1;j<=i;j++)binom[i][j]=binom[i-1][j-1]+binom[i-1][j];}
  ll *pre=malloc(sizeof(ll)*K*(n*n+2)); int done=0;
  for(int u=N-1;u>=0;u--){
    if(!isT[u])continue;
    if(u==zi){P[u][0]=1;done++;continue;}
    for(int l=0;l<=maxL;l++)bn[l]=0;
    vst[u]=u; bk[Ln[u]][bn[Ln[u]]++]=u; ll F[K]; memset(F,0,sizeof F); int lu=Ln[u];
    for(int l=lu;l<=lz;l++) for(int bi=0;bi<bn[l];bi++){int a=bk[l][bi];
      /* finalize a: R_{u,a} from in-edges if a!=u */
      int din=(int)(inS[a+1]-inS[a]);
      memset(pre,0,sizeof(ll)*K*(din+1));
      if(a!=u){ ll Rt[K];memset(Rt,0,sizeof Rt);
        for(int q=0;q<din;q++){ll e=inS[a]+q; for(int k=0;k<K;k++)pre[(q+1)*K+k]=pre[q*K+k]+(est[e]==u?G[e][k]:0);}
        for(int k=0;k<K;k++)Rt[k]=pre[din*K+k];
        int ll_=Ln[a]-lu; ll R[K];memset(R,0,sizeof R);
        for(int k=0;k<K;k++)if(Rt[k]){int sh=(ll_-k)/2;for(int j=0;j<=k;j++)R[sh+j]+=Rt[k]*binom[k][j]*(((k-j)&1)?-1:1);}
        int r=repI[a]; for(int i=0;i<K;i++)if(R[i])for(int j=0;i+j<K;j++)F[i+j]+=R[i]*P[r][j];
      }
      for(ll oe=outS[a];oe<outS[a+1];oe++){ll e=outSlot[oe]; int b=outDst[oe]; int nz=0;
        if(a==u){memset(G[e],0,sizeof(ll)*K);G[e][1]=1;nz=1;}
        else{ll*pp=pre+(ll)outPos[oe]*K; G[e][0]=0; for(int k=0;k<K-1;k++){G[e][k+1]=pp[k];if(pp[k])nz=1;}}
        if(nz){est[e]=u; if(vst[b]!=u){vst[b]=u;bk[Ln[b]][bn[Ln[b]]++]=b;}}
      }
    }
    int l=lz-lu; for(int i=0;2*i<l;i++)P[u][i]=-F[i];
    done++; if(done%200==0)fprintf(stderr,"done %d/%d len %d %.1fs\n",done,nT,lu,(double)(clock()-T0)/CLOCKS_PER_SEC);
  }
  printf("P_x_z");for(int k=0;k<K;k++)printf(" %lld",P[xi][k]);printf("\n");
  printf("lx %d lz %d mu_index %d mu %lld\n",lx,lz,(lz-lx-1)/2,((lz-lx)%2)?P[xi][(lz-lx-1)/2]:0);
  if(dump)for(int u=0;u<N;u++)if(isT[u]){printf("U");for(int i=0;i<n;i++)printf(" %d",get(A[u],i)+1);printf(" :");for(int k=0;k<K;k++)printf(" %lld",P[u][k]);printf("\n");}
  fprintf(stderr,"total %.1fs\n",(double)(clock()-T0)/CLOCKS_PER_SEC);
  return 0;}
