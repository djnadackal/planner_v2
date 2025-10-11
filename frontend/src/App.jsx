import './App.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Flex, Layout, Typography } from 'antd';

const { Header, Content } = Layout;
import NavBar from './components/navBar';
import HomeView from './views/home'
import ThingView from './views/things';

const App = () => {

  return (
    <BrowserRouter>
      <Flex style={{ width: "100vw" }}>
        <Layout style={{ minHeight: '100vh', paddingLeft: '0' }}>
          <Header style={{ paddingLeft: '20px', display: 'flex', alignItems: 'center' }}>
            <Typography.Title style={{ color: 'white', margin: 0, marginRight: '25px' }} level={3}>
              Planner
            </Typography.Title>
            <NavBar />
          </Header>
          <Content style={{ padding: '0px' }}>
            <Routes>
              <Route path="/" element={<HomeView />} />
              <Route path="/things" element={<ThingView />} />
              <Route path="/things/:thingId" element={<ThingView />} />
              <Route path="/things/:thingId/tickets/:ticketId" element={<ThingView />} />
            </Routes>
          </Content>
        </Layout>
      </Flex>
    </BrowserRouter>
  );
}

export default App
