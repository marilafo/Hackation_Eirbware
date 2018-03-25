import React, {Component} from 'react';

import { StackNavigator } from 'react-navigation';

import Home from './screens/Home';
import Form from './screens/Form';
import Wait from './screens/Wait';

const App = StackNavigator({
  Home: { screen: Home },
  Form: {screen: Form},
  Wait: {screen: Wait},
},{
  initialRouteName: 'Home',
});

export default App;
