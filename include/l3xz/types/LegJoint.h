/**
 * Copyright (c) 2023 LXRobotics GmbH.
 * Author: Alexander Entinger <alexander.entinger@lxrobotics.com>
 * Contributors: https://github.com/107-systems/l3xz/graphs/contributors.
 */

#pragma once

/**************************************************************************************
 * INCLUDE
 **************************************************************************************/

#include <tuple>

#include "Leg.h"
#include "Joint.h"

/**************************************************************************************
 * NAMESPACE
 **************************************************************************************/

namespace l3xz
{

/**************************************************************************************
 * TYPEDEF
 **************************************************************************************/

typedef std::tuple<Leg, Joint> LegJointKey;

struct leg_joint_map_key_equal : public std::binary_function<LegJointKey, LegJointKey, bool>
{
  bool operator()(const LegJointKey & v0, const LegJointKey & v1) const
  {
    return (
            std::get<0>(v0) == std::get<0>(v1) &&
            std::get<1>(v0) == std::get<1>(v1)
           );
  }
};

inline LegJointKey make_key(Leg const leg, Joint const joint)
{
  return std::tuple(leg, joint);
}

/**************************************************************************************
 * NAMESPACE
 **************************************************************************************/

} /* l3xz */
