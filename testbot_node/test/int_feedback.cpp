#include <gtest/gtest.h>
#include <ros/ros.h>
#include <std_msgs/Int32.h>

/**
  * Subscribe to an Int32, publish a modified version of it
  */
class IntNodeTest : public testing::Test
{
public:
  ros::NodeHandle nh_;
  ros::Publisher pub_;
  ros::Subscriber sub_;
  int response_;
  void intCallback(const std_msgs::Int32::ConstPtr& msg)
  {
    response_ = msg->data;
    ros::shutdown();
  }

protected:
  virtual void SetUp()
  {
    pub_ = nh_.advertise<std_msgs::Int32>("in", 1);
  }
};

TEST_F(IntNodeTest, feedbackCorrect)
{
  std_msgs::Int32 msg;
  msg.data = 10;
  sub_ = nh_.subscribe("out", 1, &IntNodeTest::intCallback, dynamic_cast<IntNodeTest*>(this));
  pub_.publish(msg);

  ros::spin();

  EXPECT_EQ(msg.data + 17, response_);
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "int_feedback");
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
