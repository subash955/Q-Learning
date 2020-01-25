def nextaction(epsilon, state, actions):
    if random.uniform(0,1) < epsilon:
        return np.argmax(Q[state,:])
    else:
        return random.choice(actions)
    
def update(state, action, nextstate, reward, gamma, lr):
    Q[state,action] += lr*(reward + gamma*max(Q[nextstate,:]))
    
def Qlearning(transition, reward, states,actions,gamma,lr,a, decay):
    Q = np.zeros([len(states),len(actions)])
    for i in range(1,10000):
        state = random.choice(states)
        terminal = False
        while not terminal:
            action = next taction(a, state, actions)
            next_state, terminal = transition(state,action)
            update(state, action, next_state, reward[state], gamma, lr)
            if not terminal:
                state = next_state
            else:
                break

        lr *= decay
    return Q
