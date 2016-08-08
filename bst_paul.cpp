#include <iostream>
#include <cstdlib>

using namespace std;

class BST{

private:

  struct node
  {
     int data;
     node* left;
     node* right;
  };

  node* root;
  void AddLeafPrivate(int key, node* Ptr);
  void PrintInorderPrivate(node* Ptr);
  node* ReturnNodePrivate(int key, node* Ptr);


public:
   BST();
   node* CreateLeaf(int key);
   node* ReturnNode(int key);
   void AddLeaf(int key);
   void PrintInorder();
   int ReturnRootKey();
   void PrintChildren(int key);


};


BST::BST(){
  root = NULL;
}

BST::node* BST::CreateLeaf(int key)
{
  node* n = new node;
  n->data = key;
  n->left = NULL;
  n->right = NULL;

  return n;
}

void BST::AddLeaf(int key)
{
  AddLeafPrivate(key, root);
}

void BST::AddLeafPrivate(int key, node* Ptr)
{
  if(root == NULL){
   root = CreateLeaf(key);
  }
  else if (key < Ptr->data){
    if(Ptr->left != NULL){
      AddLeafPrivate(key, Ptr->left);
    }
    else {
      Ptr->left = CreateLeaf(key);
    }

  }
  else if (key > Ptr->data){
    if(Ptr->right != NULL){
      AddLeafPrivate(key, Ptr->right);
    }
    else
    {
      Ptr->right = CreateLeaf(key);
    }

  }
  else
  {
    cout<<"The Key  "<< key << "is already added";
  }
}


void BST::PrintInorder(){

  PrintInorderPrivate(root);
}

void BST::PrintInorderPrivate(node* Ptr){
  if(root != NULL)
  {
   if(Ptr->left != NULL){
      PrintInorderPrivate(Ptr->left);
    }
    cout<< Ptr->data << " ";
    if(Ptr->right != NULL){
      PrintInorderPrivate(Ptr->right);
    }
  }
  else
  {
    cout << "Dude go make a treee \n";
  }

}

 BST::node* BST::ReturnNode(int key)
 {
   return ReturnNodePrivate(key, root);
 }

  BST::node* BST::ReturnNodePrivate(int key, node* Ptr)
 {
   //cout<<"PTR data" << Ptr->data << "And Key to find-- "<< key << endl;
   if (Ptr != NULL)
   {
      if(Ptr->data == key)
      {
        return Ptr;
        //cout<<"PTR" << key << endl;
      }
      else{
        if(key < Ptr->data)
          {
           return ReturnNodePrivate(key, Ptr->left);
          }
        if(key > Ptr->data)
          {
           return ReturnNodePrivate(key, Ptr->right);
          }
      }
   }
   else
   {
     return NULL;
   }
 }


int BST::ReturnRootKey(){
  if (root!= NULL)
  {
     return root->data;
  }
  else
  {
     return -1000;
  }
}



void BST::PrintChildren(int key)
{
   node* Ptr = ReturnNode(key);
   if (Ptr != NULL)
   {
     Ptr->left == NULL ?  //Conditional Operator
     cout<<"Left Child = NULL\n"  :
     cout<<"Left Child = "<< Ptr->left->data <<endl;
     Ptr->right == NULL ?  //Conditional Operator
     cout<<"right Child = NULL\n" :
     cout<<"right Child = "<< Ptr->right->data <<endl;
   }
   else{
    cout << "Dude Where is the " << key << " " ;
   }
}



int main(){
  int TreeKeys[16] = {50,76,21,4,32,64,15,52,14,100,83,2,3,70,87,80};
  BST myTree;
  cout << "Printing the tree in order\n before adding no.\n";
  myTree.PrintInorder();

  for (int i = 0; i < 16; i++)
  {
    myTree.AddLeaf(TreeKeys[i]);
  }

  cout << "Printing the tree in order\n AFTER adding no.\n";
  myTree.PrintInorder();
  cout << "\n";

  for (int j = 0; j < 16; j++)
  {
    cout<<"Treekey PArent "<<TreeKeys[j];
    cout<<endl;
    myTree.PrintChildren(TreeKeys[j]);
    cout<<endl;
  }
  cout << "\n";
  cout << "\n";
  return 0;

}
