#include <ros/ros.h>
#include <std_msgs/Int32.h>

/**
  * Subscribe to an Int32, publish a modified version of it
  */
class IntNode
{
  ros::NodeHandle nh_;
  ros::Publisher pub_;
  ros::Subscriber sub_;
  void intCallback(const std_msgs::Int32::ConstPtr& msg)
  {
    std_msgs::Int32 response;
    response.data = msg->data + 17;
    pub_.publish(response);
  }

public:
  IntNode()
  {
    pub_ = nh_.advertise<std_msgs::Int32>("out", 1);
    sub_ = nh_.subscribe("in", 1, &IntNode::intCallback, this);
  }
};

int main(int argc, char** argv)
{
  ros::init(argc, argv, "node");
  IntNode int_node;

  ros::spin();
}
