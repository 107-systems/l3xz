/**
 * Copyright (c) 2023 LXRobotics GmbH.
 * Author: Alexander Entinger <alexander.entinger@lxrobotics.com>
 * Contributors: https://github.com/107-systems/l3xz/graphs/contributors.
 */

#pragma once

/**************************************************************************************
 * INCLUDE
 **************************************************************************************/

#include <string>

/**************************************************************************************
 * NAMESPACE
 **************************************************************************************/

namespace l3xz
{

/**************************************************************************************
 * TYPEDEF
 **************************************************************************************/

enum class Joint
{
  Coxa, Femur, Tibia
};

/**************************************************************************************
 * FUNCTION DECLARATION
 **************************************************************************************/

std::string JointToStr(Joint const joint);

/**************************************************************************************
 * NAMESPACE
 **************************************************************************************/

} /* l3xz */
