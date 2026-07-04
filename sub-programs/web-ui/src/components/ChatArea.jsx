import React, { useEffect, useRef } from 'react';
import { marked } from 'marked';

// Configure marked options
marked.setOptions({
  breaks: true,
  gfm: true
});

const ChatArea = ({ history, agentDetails }) => {
  const scrollRef = useRef(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [history]);

  const renderMessage = (msg, idx) => {
    const isUser = msg.type === 'user';
    const isSystem = msg.type === 'system';
    
    if (isSystem) {
      return (
        <div key={idx} style={{
          display: 'flex',
          justifyContent: 'center',
          margin: '16px 0'
        }}>
          <span style={{
            backgroundColor: 'var(--bg-surface)',
            color: 'var(--accent-warning)',
            padding: '4px 12px',
            borderRadius: '12px',
            fontSize: '0.8rem',
            fontStyle: 'italic',
            border: '1px solid var(--glass-border)'
          }}>
            [SYS] {msg.content}
          </span>
        </div>
      );
    }

    const agentDisplayName = !isUser && !isSystem && msg.agent && agentDetails && agentDetails[msg.agent]?.AI_NAME
      ? agentDetails[msg.agent].AI_NAME
      : msg.agent || 'Agent';

    return (
      <div key={idx} style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: isUser ? 'flex-end' : 'flex-start',
        marginBottom: '20px'
      }}>
        <div style={{
          fontSize: '0.8rem',
          color: 'var(--text-muted)',
          marginBottom: '4px',
          marginLeft: isUser ? '0' : '12px',
          marginRight: isUser ? '12px' : '0'
        }}>
          {isUser ? 'You' : agentDisplayName} {msg.channel && msg.channel !== 'Web' ? `[${msg.channel}]` : ''}
        </div>
        <div 
          className={`markdown-content ${isUser ? 'user-msg-container' : ''}`}
          style={{
            maxWidth: '80%',
            padding: '12px 16px',
            borderRadius: '16px',
            backgroundColor: isUser ? 'var(--accent-primary)' : 'var(--bg-surface)',
            color: isUser ? '#11111b' : 'var(--text-main)',
            borderBottomRightRadius: isUser ? '4px' : '16px',
            borderBottomLeftRadius: isUser ? '16px' : '4px',
            boxShadow: 'var(--glass-shadow)',
            border: isUser ? 'none' : '1px solid var(--glass-border)',
            lineHeight: '1.5'
          }}
          dangerouslySetInnerHTML={{ __html: marked.parse(msg.content) }}
        />
      </div>
    );
  };

  return (
    <div style={{
      flex: 1,
      overflowY: 'auto',
      padding: '24px',
      display: 'flex',
      flexDirection: 'column'
    }} ref={scrollRef}>
      {history.length === 0 ? (
        <div style={{
          margin: 'auto',
          color: 'var(--text-muted)',
          textAlign: 'center',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: '12px'
        }}>
          <div style={{
            width: '64px',
            height: '64px',
            borderRadius: '50%',
            backgroundColor: 'var(--bg-surface)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '24px'
          }}>🤖</div>
          <p>No messages yet.</p>
          <p style={{ fontSize: '0.85rem' }}>Select an agent and start chatting!</p>
        </div>
      ) : (
        history.map((msg, idx) => renderMessage(msg, idx))
      )}
    </div>
  );
};

export default ChatArea;
