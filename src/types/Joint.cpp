/**
 * Copyright (c) 2023 LXRobotics GmbH.
 * Author: Alexander Entinger <alexander.entinger@lxrobotics.com>
 * Contributors: https://github.com/107-systems/l3xz/graphs/contributors.
 */

/**************************************************************************************
 * INCLUDE
 **************************************************************************************/

#include <l3xz/types/Joint.h>

/**************************************************************************************
 * NAMESPACE
 **************************************************************************************/

namespace l3xz
{

/**************************************************************************************
 * FUNCTION DEFINITION
 **************************************************************************************/

std::string JointToStr(Joint const joint)
{
  switch(joint)
  {
    case Joint::Coxa:  return std::string("coxa");  break;
    case Joint::Femur: return std::string("femur"); break;
    case Joint::Tibia: return std::string("tibia"); break;
    default: __builtin_unreachable();
  }
}

/**************************************************************************************
 * NAMESPACE
 **************************************************************************************/

} /* l3xz */
