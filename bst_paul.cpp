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
   if (Ptr != NULL)
   {
      if(Ptr->data == key)
      {
        return Ptr;
      }
      else{
        if(Ptr->data < key)
          {
           return ReturnNodePrivate(key, Ptr->left);
          }
        if(Ptr->data > key)
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

  return 0;

}
