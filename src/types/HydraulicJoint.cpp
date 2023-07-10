/**
 * Copyright (c) 2023 LXRobotics GmbH.
 * Author: Alexander Entinger <alexander.entinger@lxrobotics.com>
 * Contributors: https://github.com/107-systems/l3xz/graphs/contributors.
 */

/**************************************************************************************
 * INCLUDE
 **************************************************************************************/

#include <l3xz/types/HydraulicJoint.h>

/**************************************************************************************
 * NAMESPACE
 **************************************************************************************/

namespace l3xz
{

/**************************************************************************************
 * FUNCTION DEFINITION
 **************************************************************************************/

std::string JointToStr(HydraulicJoint const joint)
{
  switch(joint)
  {
    case HydraulicJoint::Femur: return std::string("femur"); break;
    case HydraulicJoint::Tibia: return std::string("tibia"); break;
    default: __builtin_unreachable();
  }
}

/**************************************************************************************
 * NAMESPACE
 **************************************************************************************/

} /* l3xz */
