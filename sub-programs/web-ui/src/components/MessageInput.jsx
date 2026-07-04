import React, { useState, useRef, useEffect } from 'react';

const MessageInput = ({ onSend, currentAgent, agentDetails }) => {
  const [inputValue, setInputValue] = useState('');
  const textareaRef = useRef(null);
  
  const displayName = agentDetails && agentDetails[currentAgent]?.AI_NAME 
    ? agentDetails[currentAgent].AI_NAME 
    : currentAgent;

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = textareaRef.current.scrollHeight + 'px';
    }
  }, [inputValue]);

  const handleSubmit = (e) => {
    if (e && e.preventDefault) e.preventDefault();
    if (!inputValue.trim()) return;
    onSend(inputValue);
    setInputValue('');
  };

  return (
    <form onSubmit={handleSubmit} style={{
      padding: '20px',
      backgroundColor: 'var(--bg-sidebar)',
      borderTop: '1px solid var(--glass-border)',
      display: 'flex',
      gap: '12px',
      alignItems: 'center'
    }}>
      <textarea
        ref={textareaRef}
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
          }
        }}
        rows={1}
        placeholder={`Ask ${displayName || 'agent'} anything...`}
        style={{
          flex: 1,
          backgroundColor: 'var(--bg-main)',
          border: '1px solid var(--glass-border)',
          borderRadius: '24px',
          padding: '14px 24px',
          color: 'var(--text-main)',
          fontSize: '1rem',
          fontFamily: 'inherit',
          outline: 'none',
          transition: 'all 0.2s',
          resize: 'none',
          overflowY: 'auto',
          maxHeight: '200px',
          lineHeight: '1.5'
        }}
        onFocus={(e) => {
          e.target.style.borderColor = 'var(--accent-primary)';
          e.target.style.boxShadow = '0 0 0 2px rgba(137, 180, 250, 0.2)';
        }}
        onBlur={(e) => {
          e.target.style.borderColor = 'var(--glass-border)';
          e.target.style.boxShadow = 'none';
        }}
      />
      <button
        type="submit"
        disabled={!inputValue.trim()}
        style={{
          backgroundColor: inputValue.trim() ? 'var(--accent-primary)' : 'var(--bg-surface)',
          color: inputValue.trim() ? '#11111b' : 'var(--text-muted)',
          border: 'none',
          borderRadius: '50%',
          width: '50px',
          height: '50px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          cursor: inputValue.trim() ? 'pointer' : 'not-allowed',
          transition: 'all 0.2s',
          boxShadow: inputValue.trim() ? '0 4px 12px rgba(137, 180, 250, 0.3)' : 'none'
        }}
        onMouseEnter={(e) => {
          if (inputValue.trim()) {
            e.currentTarget.style.transform = 'scale(1.05)';
            e.currentTarget.style.backgroundColor = 'var(--accent-primary-hover)';
          }
        }}
        onMouseLeave={(e) => {
          if (inputValue.trim()) {
            e.currentTarget.style.transform = 'scale(1)';
            e.currentTarget.style.backgroundColor = 'var(--accent-primary)';
          }
        }}
      >
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <line x1="22" y1="2" x2="11" y2="13"></line>
          <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
        </svg>
      </button>
    </form>
  );
};

export default MessageInput;
