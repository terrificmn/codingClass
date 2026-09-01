#include <iostream>
#include <list>
using std::cout;
using std::endl;
using std::string;

class MyClass {
private:
    string Name;
    string Owner;
    int SubscribersCount;
    list<string> PublishedVideoTitles;
public:
    MyClass (string name, string ownerName) {
        Name = name;
        Owner = ownerName;
        SubscribersCount = 0;
    }

    void GetInfo() {
        cout << "name: " << Name << endl;
        cout << "OwnerName: " << Owner << endl;
        cout << "SubscribersCount: " << SubscribersCount << endl;
        cout << "Videos: " << endl;

        for (string videoTitle : PublishedVideoTitles) {
            cout << videoTitle << endl;
        }
    }

    void Subscribe() {
        SubscribersCount++;
    }

    void Unsubscribe() {
        if(SubscribersCount > 0) 
            SubscribersCount--;
    }

    void PublishVideo(string title) {
        PublishedVideoTitles.push_back(title);
    }

};


// inheritance
class CookingYoutubeChannel:public MyClass{
    // 상속을 받았어도 생성자는 있어야함
public:
    // 생성자에서도 상속을 이용해서 넘겨줄 수 있다 MyClass로 넘겨준다
    CookingYoutubeChannel(string name, stringjkl;
     owner):MyClass(name, owner) {

    }
};

int main() {

    CookingYoutubeChannel myChannel("Mark Kitchen", "Mark");
    // 상속을 받았으므로 메소드를 사용할 수 있다
    myChannel.PublishVideo("Apple pie");
    myChannel.PublishVideo("choco pie");
    myChannel.GetInfo();

    //cout << namespace25::age << endl;
    //cout << namespace25::name << endl;


}