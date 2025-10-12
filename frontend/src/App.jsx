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
        <Layout style={{
          minHeight: '100vh',
          paddingLeft: '0'
        }}>
          <Header style={{
            paddingLeft: '20px',
            display: 'flex',
            alignItems: 'center'
          }}>
            <Typography.Title style={{
              color: 'white',
              margin: 0,
              marginRight: '25px'
            }} level={3}>
              Planner
            </Typography.Title>
          </Header>
          <Content style={{
            height: 'calc(100vh - 64px)',
            overflow: 'auto',
            padding: '10px'
          }}>
            <Routes>
              <Route path="/" element={<ThingView />} />
              <Route path="/tickets/:ticketId" element={<ThingView />} />
              <Route path="/:thingId" element={<ThingView />} />
              <Route path="/:thingId/tickets/:ticketId" element={<ThingView />} />
            </Routes>
          </Content>
        </Layout>
      </Flex>
    </BrowserRouter>
  );
}

export default App
