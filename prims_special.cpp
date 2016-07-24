using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)
#define scan(n) scanf("%d", &n)
#define scans(s) scanf("%s", s)
#define scanc(c) scanf("%c", &c)
#define scanp(f) scanf("%f", &f)
#define print(n) printf("%d\n", n)
#define prints(s) printf("%s\n", s)
#define printc(c) printf("%c\n", c)
#define printp(f) printf("%f\n", f)
#define nline printf("\n")
#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int

#define PB push_back
#define SZ size
#define MP make_pair

int dist[3005], parent[3005];
bool vis[3005];

std::vector<int> adj[3003];

int mat[3005][3005];

queue<pair<int,int> > pro;

int n, e;

int main()
{
    int i, j;

    int cases;

    //scan(cases);

    //wl(cases)
    {
        cin>>n>>e;
        fl(i,0,n+1)
        {
            adj[i].clear();
            vis[i]=0;
            parent[i]=-1;
            dist[i]=INT_MAX;

        }
        fl(i,0,n+1)
            fl(j,0,n+1)
            {
                mat[i][j]=INT_MAX;
                if(i==j)
                    mat[i][j]=0;
        }
        fl(i,0,e)
        {
            int x, y;
            cin>>x>>y;
            adj[x].PB(y);
            adj[y].PB(x);
            int val;
            cin>>val;
            mat[x][y]=mat[y][x]=min(val,mat[x][y]);
        }
        int ini;
        cin>>ini;

        int node=ini;
        cout << "node = cin = ini start " << node<< "\n";
        dist[node]=0;
        vis[node]=1;
        cout<< "dist ..outside while. " << dist[0] << " " <<dist[1] << " " <<dist[2] << " " << dist[3] << " " << dist[4]<<" "<< dist[5]<< "\n";
        while(1)
        {


            fl(i,0,n-1)
            {
                cout << "------------------------------------------NEW I-----------------------";
                int this_dist=INT_MAX;
                //Find the node with the minimum distance
                fl(j,1,n+1)
                {
                cout << "Find the node with the minimum di.... Checking...If,,,"<< " " << "i " << " " << i << " " <<"j " << j<< "\n";
                cout << "d1 above IFFFF. to find min dist " << dist[0] << " " <<dist[1] << " " <<dist[2] << " " << dist[3] << " " << dist[4]<< " "<< dist[5]<< "\n";
                    if(!vis[j] && dist[j]<this_dist)
                    {
                        cout << "inside if when " << "node" << j << "unvisited and dist[nownode] is lesser"<< "\n";
                        this_dist=dist[j];
                        node=j;
                        cout << "node thus selected the index of dist that gives min d" << " " << "\n";

                    }
                }

                //mark this node as visited
         cout<< "mark this " << node << "as visited after if block " << dist[0] << " " <<dist[1] << " " <<dist[2] << " " << dist[3] << " " << dist[4]<<" "<< dist[5]<< "\n";

                vis[node]=1;
                int limit=adj[node].SZ();
                cout << "limit size of adj[node]" << limit << "where node is marked one" << "\n";

                fl(j,0,limit)
                {
                  cout << "inside the limit loop " << "\n";
                  cout << "node " << node << " j " << j << "\n";
                  cout << "adj[node].j"<<" " << adj[node][j] << "\n";


                    if(!vis[adj[node][j]] && mat[node][adj[node][j]]<dist[adj[node][j]])
                    {
                        cout << "INside IF condn that adj[node][j] notvisited " << " " << adj[node][j] << " mat[node][adj[node][j]] < dist[adj[node][j]] --->" << " : "<< mat[node][adj[node][j]] << " < " << dist[adj[node][j]] << "\n";
                        dist[adj[node][j]]=mat[node][adj[node][j]];
                        cout<< "updating the dist array" << dist[0] << " " <<dist[1] << " " <<dist[2] << " " << dist[3] << " " << dist[4]<< " "<< dist[5]<< "\n";
                        cout << "setting parent node --> ob expressu --->parent[adj[node][j]]=node;";
                        parent[adj[node][j]]=node;
                    }
                }

            }

            int f=0;

            fl(i,1,n+1)
            {
                if(dist[i]==INT_MAX)
                {
                    node=i;
                    dist[node]=0;
                    vis[node]=1;
                    parent[node]=node;
                    f=1;
                    break;

                }
            }
            if(f==0)
                break;
        }

        ll ans=0;
        fl(i,1,n+1)
        {
            if(i!=ini && dist[i]!=INT_MAX)
                ans+=mat[i][parent[i]];
        }
        cout<<ans;
        nline;



    }

    return 0;
}
