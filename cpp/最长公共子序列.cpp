
/*
最长公共子序列
Description

给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。


Input

输入第一行为用例个数， 每个测试用例输入为两行，一行一个字符串


Output

如果没有公共子序列，不输出，如果有多个则分为多行，按字典序排序。

Sample Input 1
1
1A2BD3G4H56JK
23EFG4I5J6K7

Sample Output 1
23G456K
23G45JK
*/


#include <iostream>
#include <sstream>
#include <vector>
#include <set>

using namespace std;


void printPath(string strFirst,string strSecond,vector<vector<int>>& dp,int i,int j,string temp,set<string>& res)
{
	if(i>= strFirst.size()||j>=strSecond.size())
	{
		if(temp.size() == dp[strFirst.size()][strSecond.size()])
		{
			res.insert(temp);
		}

		return;
	}
	if(strFirst[i] == strSecond[j])
	{
		temp.push_back(strFirst[i]);
		printPath(strFirst,strSecond,dp,i+1,j+1,temp,res);
	}
	else if(dp[i+1][j] > dp[i][j+1])
	{
		printPath(strFirst,strSecond,dp,i+1,j,temp,res);
	}

	else if(dp[i][j+1] > dp[i+1][j])
	{
		printPath(strFirst,strSecond,dp,i,j+1,temp,res);
	}
	else
	{
		printPath(strFirst,strSecond,dp,i+1,j,temp,res);
		printPath(strFirst,strSecond,dp,i,j+1,temp,res);
	}
}
int main()
{

	int T;

	string strT;

	getline(cin,strT);

	stringstream ssT(strT);
	ssT >> T;

	while(T)
	{

		string strFirst;
		getline(cin,strFirst);
		string clearStr;
		for(int i=0;i<strFirst.size();i++)
        {
            if(strFirst[i]!=' ')
            {

                clearStr += strFirst[i];
            }
        }
        strFirst = clearStr;

        clearStr.clear();
		string strSecond;
		getline(cin,strSecond);

		for(int i=0;i<strSecond.size();i++)
		{
			if(strSecond[i]!=' ')
			{
				clearStr += strSecond[i];
			}
		}
		strSecond = clearStr;


		//cout<<strFirst<<"  "<<strSecond<<endl;

		int n=strFirst.size();
		int m=strSecond.size();

		vector<vector<int>> dp(n+1,vector<int>(m+1,0));
		vector<vector<int>> path(n+1,vector<int>(m+1,0));
		string temp;
		set<string> res;
		for(int i=1;i<=n;i++)
		{

			for(int j=1;j<=m;j++)
			{

				if(strSecond[j-1] == strFirst[i-1])
				{
					path[i][j] = 1;
					dp[i][j] = dp[i-1][j-1]+1;
				}
				else
				{
					if(dp[i][j-1] > dp[i-1][j])
					{
						path[i][j] = 2;
						dp[i][j] = dp[i][j-1];
					}
					else
					{
						path[i][j] = 3;
						dp[i][j] = dp[i-1][j];
					}
					//dp[i][j] = max(dp[i][j-1],dp[i-1][j]);

				}

			}

		}
		/*

		for(int i=1;i<n+1;i++)
        {

            for(int j=1;j<m+1;j++)
            {

                cout<<dp[i][j]<<" ";
            }
            cout<<endl;
        }

        cout<<endl;

        for(int i=1;i<n+1;i++)
        {

            for(int j=1;j<m+1;j++)
            {

                cout<<path[i][j]<<" ";
            }
            cout<<endl;
        }
        */

		printPath(strFirst,strSecond,dp,0,0,temp,res);
		/*

		for(int i=0;i<res.size();i++)
		{
			cout<<res[i]<<endl;
		}

		cout<<dp[n][m]<<endl;
		*/
		for(set<string>::iterator i = res.begin();i!=res.end();i++)
		{
			cout<<*i<<endl;
		}

		T--;
	}
	return 0;
}
