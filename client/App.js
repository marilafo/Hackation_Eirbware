import React, {Component} from 'react';

import { StackNavigator } from 'react-navigation';

import Home from './screens/Home';

const App = StackNavigator({
  Home: { screen: Home },
},{
  initialRouteName: 'Home',
});

export default App;
