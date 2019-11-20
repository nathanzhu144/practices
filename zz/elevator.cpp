#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <utility>
#include <set>

using namespace std;

class Request{
public:
    Request(int start_f, int end_f) : start_floor(start_f), end_floor(end_f) {}
    int start_floor;
    int end_floor;
};

static int id_creator = 0;

class Elevator{
public:
    Elevator(int max_floor_in, int min_floor_in):
             state("bottom"), max_floor(max_floor_in), min_floor(min_floor_in) {}

    void add_requests(vector<Request> req){
        destinations = req;
    }

    void move_up(){
        set<int> visit;
        for(auto i : destinations){
            visit.insert(i.end_floor);
        }
        destinations.clear();

        for(int i = min_floor; i < max_floor; ++i){
            if(visit.count(i) != 0)
                cout << "Elevator up " << id << " stopped on floor " << i << endl;
        }
        state = "top";
    }

    void move_down(){
        set<int> visit;
        for(auto i : destinations){
            visit.insert(i.end_floor);
        }
        destinations.clear();

        for(int i = max_floor; i < min_floor; ++i){
            if(visit.count(i) != 0)
                cout << "Elevator down " << id << " stopped on floor " << i << endl;
        }
        state = "bottom";
    }

    vector<Request> destinations;
    string state;
    int max_floor;
    int min_floor;
    int id = id_creator++;
};


class Manager{
    public:

    Manager(int num_el){
        for(int i = 0; i < num_el; ++i) 
            elevators.push_back(Elevator(10, 1));
    }

    void start_producer(){
        while(true){

        }
    }

    void start_consumer(int elevator_id){
        while(true){
            if(elevators[elevator_id].state == "bottom"){
                // we are going up 
                upmutex.lock();
                while(up.empty()){
                    upconsumers.wait(upmutex);
                }
                // At this point has a lock on up.
                elevators[elevator_id].add_requests(up);
                upmutex.unlock();

                elevators[elevator_id].move_up();
            }
            if(elevators[elevator_id].state == "top"){
                downmutex.lock();
                while(down.empty()){
                    downconsumers.wait(downmutex);
                }

                elevators[elevator_id].add_requests(down);
                downmutex.unlock();

                elevators[elevator_id].move_down();
            }
        }
    }

    void add_request(Request& r){
        if(r.start_floor < r.end_floor){
            upmutex.lock();
            up.push_back(r);
            upmutex.unlock();
        }
        else{
            downmutex.lock();
            down.push_back(r);
            downmutex.unlock();
        }
    }

    std::thread start_producer_thread(){
        return std::thread([this] {this->start_producer; });
    }

    std::thread start_consumer_thread(){
        return std::thread([this] {this->start_producer; });
    }


    private:
    std::condition_variable producers;
    std::condition_variable downconsumers;
    std::condition_variable upconsumers;
    mutex downmutex;
    mutex upmutex;
    vector<Request> down;
    vector<Request> up;
    vector<Elevator> elevators;
};



int main(){
    return 0;
}